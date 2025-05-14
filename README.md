# mong-mcp-server

A Model Context Protocol (MCP) server implementation that provides a [moby](https://github.com/moby/moby)-like random name generator ("[mong](https://github.com/toshihikoyanase/mong/)") for use with tools like Claude Desktop and VS Code Copilot Agent.

## Features

- Exposes a moby-like random name generator through the MCP interface
- Easy setup and configuration

## Configuration for Claude Desktop

Add this server under the `mcpServers` key of Claude Desktop configuration.
See the [official document of the Model Context Protocol](https://modelcontextprotocol.io/quickstart/user) for details.

```json
{
   "mcpServers": {
      "mong": {
         "command": "uvx",
         "args": [
            "--from",
            "git+https://github.com/toshihikoyanase/mong-mcp-server",
            "mong-mcp"
         ]
      }
   }
}
```

or

```json
{
    "mcpServers": {
        "mong": {
            "command": "uv",
            "args": [
                "--directory",
                "/path/to/repository",
                "run",
                "python",
                "-m",
                "mong_mcp_server"
            ]
        }
    }
}
```

## Configuration for VS Code Copilot Agent

Add this server under the `servers` key in your MCP configuration for VS Code.
For example, to enable the MCP server in your workspace, create a `.vscode/mcp.json` file as follows:

```json
{
    "servers": {
        "mong": {
            "type": "stdio",
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/toshihikoyanase/mong-mcp-server",
                "mong-mcp"
            ]
        }
    }
}
```

## Install locally

1. **Clone the repository:**
    ```sh
    git clone https://github.com/toshihikoyanase/mong-mcp-server.git
    cd mong-mcp-server
    ```

2. **Start the server:**
    ```sh
    uv run python main.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
