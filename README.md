# Optics agent plugins

Agent plugins and skills for [Optics](https://optics-framework.org) (`optics-framework` on PyPI),
open-source test automation for Android, iOS, Android TV, Samsung Tizen, LG webOS and web.

This repo is three things at once:

- a **Claude Code plugin marketplace** with one plugin, `optics-framework`, which adds the Optics
  MCP server and a skill that teaches the agent the Optics suite format;
- a **Cursor plugin** repo with the same plugin, for the Cursor Marketplace;
- a **skills repo** that [skills.sh](https://skills.sh) can install into Claude Code, Cursor,
  Codex and other agents.

With it, your agent can open a session on a phone, TV or browser, look at the screen, tap and
type, and then write what it did as a CSV or YAML test suite that `optics execute` runs in CI.

## What's inside

```text
.claude-plugin/marketplace.json                          Claude Code marketplace "optics-agent-plugins"
.cursor-plugin/marketplace.json                          Cursor marketplace manifest
plugins/optics-framework/
  .claude-plugin/plugin.json                             Claude Code plugin manifest
  .cursor-plugin/plugin.json                             Cursor plugin manifest
  .mcp.json                                              starts `optics mcp` (optics-framework 1.11.0), used by both
  skills/optics-framework/SKILL.md                       the skill (shared by Claude Code, Cursor and skills.sh)
  assets/logo.svg, logo-plate.svg                        logo (transparent, and on a white plate)
```

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) on your `PATH`. The plugin starts
  the server with `uvx`, which fetches Python 3.12+ and `optics-framework` 1.11.0 for you.
- For Android, iOS and TV: a running [Appium](https://appium.io) server with the UiAutomator2 or
  XCUITest driver. See [Test Android apps](https://optics-framework.org/docs/platforms/android)
  and [Test iOS apps](https://optics-framework.org/docs/platforms/ios).
- For web: a Playwright Chromium build. Install it once:

  ```shell
  uvx --from "optics-framework[mcp,appium,playwright]==1.11.0" playwright install chromium
  ```

The first start downloads the package and can take a minute or two. Claude Code gives an MCP
server 30 seconds to start, so on a fresh machine the server shows as failed in `/mcp` until the
download finishes. Warm the cache once before you start your agent:

```shell
uvx --from "optics-framework[mcp,appium,playwright]==1.11.0" optics --version
```

Or start Claude Code with a longer limit, such as `MCP_TIMEOUT=180000 claude`.

## Install in Claude Code

```text
/plugin marketplace add mozarkai/optics-agent-plugins
/plugin install optics-framework@optics-agent-plugins
```

Or from your shell:

```shell
claude plugin marketplace add mozarkai/optics-agent-plugins
claude plugin install optics-framework@optics-agent-plugins
```

Then ask something like "open https://example.com in a browser with Optics and list what's on the
page".

## Install in Cursor

Once the plugin is listed in the [Cursor Marketplace](https://cursor.com/marketplace), open
**Customize**, search for "Optics" and select **Install**. To try it before then, copy
`plugins/optics-framework` to `~/.cursor/plugins/local/optics-framework` and reload the window.
The same uv requirement and first-start download apply.

## Install the skill with skills.sh

```shell
npx skills add mozarkai/optics-agent-plugins
```

This installs only the skill. Add the MCP server to your agent yourself, as below.

## Use the MCP server with another client

Add this to your client's MCP config (Claude Desktop, Cursor, VS Code, and others use the same
shape):

```json
{
  "mcpServers": {
    "optics": {
      "command": "uvx",
      "args": ["--from", "optics-framework[mcp,appium,playwright]==1.11.0", "optics", "mcp"]
    }
  }
}
```

Without uv, install the package with pip (Python 3.12 or newer) and point the client at
`optics mcp`:

```shell
pip install "optics-framework[mcp,appium,playwright]==1.11.0"
```

```json
{ "mcpServers": { "optics": { "command": "optics", "args": ["mcp"] } } }
```

If the client can't find `optics`, use its full path (`which optics`).

## Learn more

- [Optics docs](https://optics-framework.org/docs/get-started/index.md) and the
  [docs index for agents](https://optics-framework.org/docs/llms.txt)
- [MCP server reference](https://optics-framework.org/docs/reference/mcp.md): every tool,
  resource and environment variable
- [Let your AI agent build tests](https://optics-framework.org/docs/create/agent.md)
- [optics-framework on GitHub](https://github.com/mozarkai/optics-framework)

## License

[Apache-2.0](LICENSE)
