from mcp.server.fastmcp import FastMCP
import mong


def main() -> None:
    mcp = FastMCP("mong-mcp-server", "MCP server to generate Docker-like random names")

    @mcp.tool(
        name="get_random_name",
        description="Generate a random name like Docker does."
    )
    def get_random_name() -> str:
        """Tool to Generate Docker-Like Random Names"""
        return mong.get_random_name()

    mcp.run()
