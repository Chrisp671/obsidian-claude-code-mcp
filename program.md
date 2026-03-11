# MCP Improvement Program

> Autoresearch-style program for iteratively improving the Obsidian Claude Code MCP plugin.
> Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## Context

This is an Obsidian plugin providing MCP (Model Context Protocol) servers for Claude Code and Claude Desktop integration. Read `CLAUDE.md` for full architecture details.

Key files to understand:
- `main.ts` — Plugin entry, terminal toggle, server lifecycle
- `src/mcp/dual-server.ts` — Manages WebSocket + HTTP servers
- `src/mcp/server.ts` — WebSocket server (Claude Code auto-discovery)
- `src/mcp/http-server.ts` — HTTP/SSE server (Claude Desktop)
- `src/terminal/terminal-view.ts` — Embedded terminal using xterm.js
- `src/settings.ts` — Plugin settings UI
- `src/shared/tool-registry.ts` — Tool registration system

## Improvement Targets

### 1. Multiple Terminal Sessions (max 4)

**Current state:** `toggleClaudeTerminal()` in `main.ts` only allows ONE terminal at a time. It checks `getLeavesOfType(TERMINAL_VIEW_TYPE)[0]` and reuses/closes if found.

**Goal:** Support up to 4 concurrent terminal sessions, each running its own Claude instance.

**Changes needed:**
- Remove single-instance terminal check in `main.ts:toggleClaudeTerminal()`
- Add session numbering (Terminal 1, Terminal 2, etc.)
- Add `maxTerminalSessions` setting (default: 4) to `src/settings.ts`
- Update `getDisplayText()` in `terminal-view.ts` to show session number
- Each terminal gets its own shell process and MCP environment variables
- Add a "New Terminal" command alongside "Toggle Terminal"
- The ribbon icon should create a new session (up to max), not toggle

### 2. Wispr Flow / Voice-to-Text in Terminals

**Current state:** The custom key event handler in `terminal-view.ts:73-113` only checks `event.type === "keydown"`. xterm.js has composition event support via CompositionHelper, but:
- Voice-to-text tools may not emit standard composition events
- The xterm.js textarea (used for IME input) may have focus issues within Obsidian
- KeyCode 229 (composition character) handling may interfere

**Goal:** Voice-to-text tools like Wispr Flow should be able to input text into the terminal.

**Changes needed:**
- Ensure the custom key handler does not block composition events
- Add explicit handling for `compositionstart`/`compositionend` events
- Consider adding a visible textarea overlay that forwards input to xterm when composition is active
- Test that `onData` receives composition-completed text

## Experiment Loop

1. Read the current state of the target files
2. Pick ONE improvement from the targets above
3. Make the minimal change needed
4. Run `bun run build` to verify no type/build errors
5. If build succeeds: commit with descriptive message
6. If build fails: fix or revert
7. Move to next improvement
8. Repeat until all targets are addressed

## Constraints

- Only modify files listed in the Context section above
- Each change should be small and focused
- Always run `bun run build` after changes
- Keep backward compatibility (existing single-terminal users should see no change in behavior)
- Follow existing code patterns (check CLAUDE.md)
