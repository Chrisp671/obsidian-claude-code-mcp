# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Zenith Bridge is an Obsidian plugin implementing dual-transport MCP (Model Context Protocol) servers: WebSocket for Claude Code CLI auto-discovery and HTTP/SSE for Claude Desktop. It also provides an optional embedded terminal with cross-platform PTY support.

See `AGENTS.md` for detailed project structure, tool definitions, terminal system, and common tasks reference.

## Development Commands

- `bun install` - Install dependencies
- `bun run dev` - Start compilation in watch mode (esbuild context with incremental rebuilds)
- `bun run build` - Type check (`tsc -noEmit -skipLibCheck`) and build for production
- `bun run version patch|minor|major` - Bump version in package.json, manifest.json, versions.json
- `eslint main.ts` - Run linting

## Architecture

### Request Flow

```
Claude Code CLI ──WebSocket──┐
                             ├── McpDualServer (dual-server.ts)
Claude Desktop ──HTTP/SSE────┘        │
                                      ├── handlers.ts: handleRequestGeneric(req, reply, source)
                                      │     │
                                      │     ├── ide-handler.ts (if ideHandler.isIdeMethod())
                                      │     │
                                      │     └── tool-registry.ts (selects registry by source)
                                      │           ├── wsToolRegistry  ← general + IDE tools
                                      │           └── httpToolRegistry ← general tools only
                                      │
                                      └── workspace-manager.ts (broadcasts selection changes)
```

The `source` parameter (`"ws"` | `"http"`) flows through handlers to select the correct tool registry. This is the key mechanism that gives Claude Code access to IDE-specific tools while standard MCP clients only see general tools.

### Dual Registry System (dual-server.ts)

`McpDualServer` maintains two separate `ToolRegistry` instances:

1. **General tools** (from `src/tools/general-tools.ts`) are registered to **both** registries
2. **IDE tools** (from `src/ide/ide-tools.ts`) are registered **only** to the WebSocket registry
3. **MCP-only tools** (from `src/tools/mcp-only-tools.ts`) would register only to HTTP registry (currently empty)

The `ToolRegistry` (`src/shared/tool-registry.ts`) enforces that each tool's definition name must match its implementation name at registration time.

### Plugin Lifecycle (main.ts)

**onload()**: Load settings → register icon → conditionally init terminal (lazy) → add settings tab → init WorkspaceManager → init McpDualServer → setup listeners

**onunload()**: Close terminal leaves → stop MCP servers → remove ribbon icon

`initializeMcpServer()` catches `EADDRINUSE` and `EACCES` specifically to show user-friendly port conflict messages.

### Lock File Discovery

The WebSocket server (`src/mcp/server.ts`) creates `[port].lock` files with an `authToken` (UUID) for Claude Code auto-discovery. Lock files are written to **both** locations for compatibility:
- `~/.config/claude/ide/` (modern, Claude Code v1.0.30+)
- `~/.claude/ide/` (legacy)

Config directory resolution is in `src/claude-config.ts` (checks `CLAUDE_CONFIG_DIR` env → `XDG_CONFIG_HOME` → defaults).

### Workspace Manager

`src/obsidian/workspace-manager.ts` uses DOM `selectionchange` events (not polling) to track the active file and selection. It validates that selections are within editable notes (checks for `cm-editor`, `CodeMirror`, `markdown-source-view` classes) and broadcasts `SelectionChangedParams` to all connected clients.

## Build System

- **Format**: CommonJS (required by Obsidian plugins)
- **Target**: ES2018
- **Special loaders**: `.py` files bundled as text strings, `.png` as data URLs
- **Externals**: `obsidian`, `electron`, all `@codemirror/*`, `@lezer/*`, and Node builtins are NOT bundled (provided by Obsidian's Electron environment)
- **Output**: Single `main.js` file (source maps inline in dev, disabled in prod)

## Testing

No automated test suite. Testing is manual:
1. `bun run build`
2. Copy `main.js`, `manifest.json`, `styles.css` to test vault's `.obsidian/plugins/zenith-bridge/`
3. Enable plugin in Obsidian, test with Claude Code (`/ide` command) and/or Claude Desktop
4. Test scripts in `scripts/`: `test-manual-requests.js` (interactive), `test-mcp-client.js` (full client)

## TypeScript Configuration

- `strictNullChecks: true` — handle nulls explicitly
- `noImplicitAny: true`
- Module: ESNext, Target: ES6

## Release Process

**Read `docs/AUTOMATED_PATCH_RELEASE.md` before creating any release.**

### Patch Releases
1. Commit with conventional messages (`fix:`, `feat:`, `docs:`, `chore:`)
2. `npm version patch` (bumps package.json + manifest.json + versions.json, creates tag)
3. `bun run build`
4. `git push && git push --tags`
5. `gh release create <version> --title "Release <version>" --notes "<notes>" manifest.json main.js styles.css`

**Important**: Obsidian doesn't use 'v' prefix in tags (use `1.2.4` not `v1.2.4`).

### Minor/Major Releases
Follow `docs/RELEASE_CHECKLIST.md`. Use `bun run version minor|major` instead of npm.

## Implementation Constraints

- **MCP Spec**: HTTP server uses legacy 2024-11-05 spec (not Streamable HTTP) — newer spec not yet supported by most clients
- **Path Safety**: All file operations restricted to vault boundaries via `normalizePath()` in `src/obsidian/utils.ts`
- **Multi-Vault**: Each vault needs a unique HTTP port (default 22360)
- **Log Prefixes**: Use `[MCP]`, `[Terminal]`, `[ToolRegistry]` for console logging
- **Error Display**: Use Obsidian's `Notice` class for user-facing errors

## Coding Guidelines

- When refactoring, don't create files with a `-refactored` suffix — carry out the refactoring in place as a senior engineer would
- Settings migration: when changing `ClaudeCodeSettings`, add migration logic in `migrateClaudeCodeSettings()` in `src/settings.ts`

## Adding New Tools

1. **Shared tools** (both transports): Add definition to `GENERAL_TOOL_DEFINITIONS` and implementation in `GeneralTools.createImplementations()` in `src/tools/general-tools.ts`
2. **IDE-only tools** (WebSocket): Add to `IDE_TOOL_DEFINITIONS` / `IdeTools.createImplementations()` in `src/ide/ide-tools.ts`
3. **MCP-only tools** (HTTP): Add to `MCP_ONLY_TOOL_DEFINITIONS` in `src/tools/mcp-only-tools.ts` and register only to `httpToolRegistry` in `dual-server.ts`

Tool handler signature: `async (args: Record<string, unknown>, reply: McpReplyFunction) => void`
