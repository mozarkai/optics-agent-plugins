"""Start the optics-framework MCP server over stdio (same as `optics mcp`)."""
import sys

from optics_framework.helper.cli import main

if __name__ == "__main__":
    sys.argv = ["optics", "mcp"]
    main()
