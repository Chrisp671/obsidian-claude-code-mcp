# AGENTS.md - Zenith Bridge for Obsidian

This file provides essential information for AI coding agents working on the Zenith Bridge Obsidian plugin.

## Project Overview

Zenith Bridge is an Obsidian plugin that implements MCP (Model Context Protocol) servers to enable Claude Code and Claude Desktop integration with Obsidian vaults. The plugin provides:

1. **Dual Transport MCP Server**:
   - WebSocket server for Claude Code CLI auto-discovery via lock files
   - HTTP/SSE server for Claude Desktop and other MCP clients

2. **Embedded Terminal** (optional):
   - Full PTY support using xterm.js
   - Multiple terminal sessions with configurable profiles
   - Platform-specific implementations (Windows ConPTY, Unix PTY, fallback child_process)

## Technology Stack

- **Language**: TypeScript (target ES6, module ESNext)
- **Build Tool**: esbuild (bundles to CommonJS)
- **Runtime**: Node.js (via Obsidian's Electron environment)
- **Package Manager**: bun (preferred) or npm

### Key Dependencies

```
Runtime:
- ws: ^8.18.2 (WebSocket server for Claude Code)
- @xterm/xterm: 5.5.0 (Terminal UI)
- @xterm/addon-fit: 0.10.0 (Terminal sizing)

Dev:
- esbuild: ^0.25.5 (Bundler)
- typescript: ^5.8.3
- obsidian: latest (Plugin API)
- @types/node, @types/ws
```

## Project Structure

```
.
├── main.ts                    # Plugin entry point (ClaudeMcpPlugin class)
├── manifest.json              # Obsidian plugin metadata
├── package.json               # NPM configuration
├── esbuild.config.mjs         # Build configuration
├── tsconfig.json              # TypeScript configuration
├── styles.css                 # Plugin styles (xterm.js + custom MCP/terminal styles)
├── version-bump.mjs           # Version management script
├── install.sh                 # Install script for test vaults
│
├── src/
│   ├── settings.ts            # Plugin settings interface, defaults, and settings UI
│   ├── claude-config.ts       # Claude config directory detection
│   │
│   ├── mcp/                   # MCP protocol implementation
│   │   ├── dual-server.ts     # Manages both WebSocket and HTTP servers
│   │   ├── server.ts          # WebSocket server (Claude Code)
│   │   ├── http-server.ts     # HTTP/SSE server (Claude Desktop)
│   │   ├── handlers.ts        # Request routing and handling
│   │   └── types.ts           # MCP TypeScript interfaces
│   │
│   ├── ide/                   # IDE-specific functionality (WebSocket only)
│   │   ├── ide-handler.ts     # IDE protocol handler
│   │   └── ide-tools.ts       # IDE-specific tools (openDiff, close_tab, etc.)
│   │
│   ├── tools/                 # MCP tool implementations
│   │   ├── general-tools.ts   # Shared tools (view, str_replace, create, insert, obsidian_api)
│   │   ├── file-tools.ts      # File operations
│   │   ├── workspace-tools.ts # Workspace operations
│   │   └── mcp-only-tools.ts  # HTTP-only tools (currently none)
│   │
│   ├── shared/                # Common utilities
│   │   └── tool-registry.ts   # Tool registration and validation system
│   │
│   ├── obsidian/              # Obsidian integration
│   │   ├── workspace-manager.ts  # Active file tracking via DOM events
│   │   └── utils.ts           # Path normalization and validation
│   │
│   └── terminal/              # Embedded terminal feature
│       ├── terminal-view.ts   # Terminal UI component using xterm.js
│       ├── terminal-manager.ts # Session management and picker
│       ├── pseudoterminal.ts  # Platform abstraction (UnixPseudoterminal, WindowsPseudoterminal, ChildProcessPseudoterminal)
│       ├── python-detection.ts # Python environment detection
│       ├── profiles.ts        # Terminal profile definitions
│       ├── unix_pseudoterminal.py.d.ts    # Type declaration for embedded Python
│       └── windows_pseudoterminal.py.d.ts # Type declaration for embedded Python
│
├── icon.svg                   # Plugin icon
│
├── docs/                      # Documentation
│   ├── AUTOMATED_PATCH_RELEASE.md  # Automated patch release process
│   ├── RELEASE_CHECKLIST.md   # Manual release checklist
│   └── COMMUNITY_SUBMISSION.md # Obsidian community plugin submission guide
│
└── scripts/                   # Testing utilities
    ├── test-manual-requests.js
    └── test-mcp-client.js
```

## Build Commands

```bash
# Development (watch mode)
bun run dev

# Production build (type check + bundle)
bun run build

# Version management
bun run version patch   # Patch release
bun run version minor   # Minor release
bun run version major   # Major release

# Linting
eslint main.ts
```

## Build System Details

- **Entry Point**: `main.ts`
- **Output**: `main.js` (CommonJS, bundled)
- **Target**: ES2018
- **Platform**: Node.js
- **Special Loaders**:
  - `.py` files → bundled as text (embedded Python scripts for PTY)
  - `.png` files → bundled as data URLs (plugin icon)
- **External Dependencies**: obsidian, electron, codemirror, lezer (not bundled)

## Code Style Guidelines

### TypeScript

- Strict null checks enabled
- Explicit return types on public methods
- Use `unknown` instead of `any` where possible
- Interfaces for data structures, types for unions

### Error Handling

- Use Obsidian's `Notice` class for user-facing errors
- Log to console with prefixes: `[MCP]`, `[Terminal]`, `[ToolRegistry]`
- Graceful degradation (e.g., fallback terminal mode)

### Naming Conventions

- Classes: `PascalCase` (e.g., `McpDualServer`)
- Interfaces: `PascalCase` with descriptive names (e.g., `McpRequest`)
- Private methods/properties: `camelCase` with `private` modifier
- Constants: `SCREAMING_SNAKE_CASE` or `PascalCase` for enum-like

### File Organization

- One class per file (generally)
- Group related functionality in directories
- Use barrel exports sparingly (prefer explicit imports)

## MCP Tool System

The plugin implements a dual registry system for tools:

### Tool Categories

1. **Shared Tools** (available to both IDE/WebSocket and MCP/HTTP clients):
   - `get_current_file` - Get the currently active file
   - `get_workspace_files` - List all files in vault
   - `view` - View file/directory contents with line numbers
   - `str_replace` - Replace text in files
   - `create` - Create new files
   - `insert` - Insert text at specific line numbers
   - `obsidian_api` - Execute Obsidian API commands

2. **IDE-specific Tools** (WebSocket only, for Claude Code):
   - `getDiagnostics` - System and vault diagnostics
   - `openDiff` - Diff view operations (stub)
   - `close_tab` - Tab management (stub)
   - `closeAllDiffTabs` - Bulk tab operations (stub)

3. **MCP-only Tools** (HTTP only):
   - Currently none, but architecture supports adding them

### Adding a New Tool

1. **For Shared Tools** (WebSocket + HTTP):
   - Add definition to `GENERAL_TOOL_DEFINITIONS` in `src/tools/general-tools.ts`
   - Add implementation in `GeneralTools.createImplementations()`
   - Automatically available to both transports

2. **For IDE-specific Tools** (WebSocket only):
   - Add definition to `IDE_TOOL_DEFINITIONS` in `src/ide/ide-tools.ts`
   - Add implementation in `IdeTools.createImplementations()`

3. **For HTTP-only Tools**:
   - Add to `MCP_ONLY_TOOL_DEFINITIONS` in `src/tools/mcp-only-tools.ts`
   - Register only to `httpToolRegistry` in `dual-server.ts`

### Tool Definition Structure

```typescript
{
  name: "tool_name",
  description: "What this tool does",
  category: "general" | "file" | "workspace" | "ide-specific",
  inputSchema: {
    type: "object",
    properties: { /* JSON Schema */ }
  }
}
```

### Implementation Structure

```typescript
{
  name: "tool_name",  // Must match definition
  handler: async (args: any, reply: McpReplyFunction) => {
    // Do work
    reply({ result: { content: [{ type: "text", text: "result" }] } });
    // Or on error:
    reply({ error: { code: -32603, message: "error message" } });
  }
}
```

## Terminal System

### PTY Mode Selection (Automatic)

| Platform | Python available | pywinpty installed | Mode used |
|----------|-----------------|-------------------|-----------|
| Windows | Yes | Yes | ConPTY via pywinpty |
| Windows | Yes | No | Fallback (child_process) |
| Windows | No | - | Fallback (child_process) |
| macOS/Linux | Yes | - | Unix PTY via stdlib |
| macOS/Linux | No | - | Fallback (child_process) |

### Terminal Profiles

Profiles define how terminals are launched:

```typescript
interface TerminalProfile {
  id: string;              // Unique identifier
  name: string;            // Display name
  launchCommand: string;   // Command to run after shell opens (e.g., "claude")
  env: Record<string, string>;  // Environment variables
  envStrategy: "claude-code" | "none";  // Whether to add Claude-specific env vars
  icon?: string;           // Obsidian icon name
  builtin?: boolean;       // True for built-in profiles (cannot be deleted)
}
```

Built-in profile: `claude` (launches `claude` command with Claude Code environment)

## Testing

### Manual Testing

1. Build: `bun run build`
2. Install to test vault: `./install.sh /path/to/vault` or copy files manually
3. Reload Obsidian and enable plugin
4. Test with Claude Code: Run `claude`, use `/ide` command, select "Obsidian"
5. Test with Claude Desktop: Configure MCP server in settings

### Test Scripts

- `scripts/test-manual-requests.js` - Interactive MCP request tester
- `scripts/test-mcp-client.js` - Full MCP client implementation

Run with: `node scripts/test-mcp-client.js`

## Release Process

### Patch Releases (Automated)

```bash
# 1. Commit changes with conventional commit messages
git commit -m "fix: description of fix"

# 2. Bump version (updates package.json, manifest.json, versions.json)
npm version patch

# 3. Build
bun run build

# 4. Push
git push && git push --tags

# 5. Create GitHub release
gh release create <version> \
  --title "Release <version>" \
  --notes "<release notes>" \
  manifest.json main.js styles.css
```

See `docs/AUTOMATED_PATCH_RELEASE.md` for detailed steps.

### Minor/Major Releases (Manual)

```bash
# 1. Bump version
bun run version minor  # or major

# 2. Test thoroughly with both Claude Code and Claude Desktop

# 3. Build and create release manually
bun run build

# 4. Create GitHub release with version tag
# Upload manifest.json, main.js, styles.css
```

See `docs/RELEASE_CHECKLIST.md` for complete checklist.

### Required Release Files

Every release must include these three files as attachments:
- `manifest.json` - Plugin metadata
- `main.js` - Compiled plugin code
- `styles.css` - Plugin styles

## Important Implementation Notes

### MCP Specification

- **HTTP Transport**: Uses legacy MCP spec 2024-11-05 (not Streamable HTTP)
- **WebSocket Transport**: Custom protocol for Claude Code integration
- **Default Port**: 22360 (configurable, must be unique per vault)

### Lock Files (Auto-Discovery)

WebSocket server creates `[port].lock` files for Claude Code discovery:
- Primary location: `~/.config/claude/ide/` (Claude Code v1.0.30+)
- Legacy location: `~/.claude/ide/`
- Contains: `authToken` (UUID generated per session), `workspaceFolders`, `ideName`
- Automatically cleaned up on plugin unload

### Path Handling

- All paths normalized via `normalizePath()` in `src/obsidian/utils.ts`
- Operations restricted to vault boundaries
- Use Obsidian's `TFile` and `TFolder` abstractions when possible

### Settings Interface

```typescript
interface ClaudeCodeSettings {
  mcpHttpPort: number;                    // Default: 22360
  enableWebSocketServer: boolean;         // Default: true
  enableHttpServer: boolean;              // Default: true
  enableEmbeddedTerminal: boolean;        // Default: true
  autoCloseTerminalOnShellExit: boolean;  // Default: true
  maxTerminalSessions: number;            // Default: 4
  defaultTerminalProfileId: string;       // Default: "claude"
  terminalProfiles: TerminalProfile[];    // Default: []
}
```

Settings are migrated from legacy formats in `migrateClaudeCodeSettings()`.

### Security Considerations

- File operations restricted to vault boundaries (via path normalization)
- Auth tokens regenerated on each Obsidian restart
- No hardcoded secrets or API keys
- `obsidian_api` tool uses `new Function()` - ensure user awareness of risks

### Multi-Vault Support

Each vault needs a unique HTTP port. The plugin detects port conflicts and provides guidance:
- Error detection for `EADDRINUSE` (port in use)
- Error detection for `EACCES` (permission denied)
- Helpful error messages guiding users to change ports

## Troubleshooting Guide

### Port Conflicts

If port 22360 is in use:
1. Change port in Settings → Community Plugins → Zenith Bridge
2. Update Claude Desktop config to match
3. Restart Claude Desktop

### Terminal Not Starting

- Verify Python 3.7+ is installed and on PATH
- Windows: Run `pip install pywinpty`
- Check Obsidian developer console (Ctrl+Shift+I) for `[Terminal]` logs

### MCP Connection Issues

- Verify plugin is enabled
- Check server status in plugin settings
- For Claude Code: Check lock files in `~/.config/claude/ide/`
- For Claude Desktop: Verify config file syntax

## Dependencies to Know

- **Obsidian API**: Core API for plugin development
- **ws**: WebSocket library for MCP server
- **@xterm/xterm**: Terminal emulator for embedded terminal
- **esbuild**: Fast bundler for TypeScript/JavaScript

## Common Tasks

### Adding a New Setting

1. Add to `ClaudeCodeSettings` interface in `src/settings.ts`
2. Add to `DEFAULT_SETTINGS` object
3. Add migration logic in `migrateClaudeCodeSettings()` if needed
4. Add UI in `ClaudeCodeSettingTab.display()`

### Modifying MCP Behavior

1. Server logic: `src/mcp/dual-server.ts`
2. Request handling: `src/mcp/handlers.ts`
3. Tool implementations: `src/tools/general-tools.ts` or `src/ide/ide-tools.ts`

### Modifying Terminal Behavior

1. UI: `src/terminal/terminal-view.ts`
2. Session management: `src/terminal/terminal-manager.ts`
3. PTY spawning: `src/terminal/pseudoterminal.ts`
4. Profiles: `src/terminal/profiles.ts`

## Resources

- [Obsidian Developer Documentation](https://docs.obsidian.md/Plugins/Getting+started)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
- [xterm.js Documentation](https://xtermjs.org/)
