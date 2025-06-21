import unittest
from unittest.mock import patch, MagicMock
from mong_mcp_server.server import main


class TestMongMCPServer(unittest.TestCase):

    @patch('mong_mcp_server.server.FastMCP')
    def test_server_initialization(self, mock_fastmcp):
        """Test that the server initializes correctly"""
        mock_mcp_instance = MagicMock()
        mock_fastmcp.return_value = mock_mcp_instance

        with patch('mong_mcp_server.server.FastMCP.run'):
            main()

        mock_fastmcp.assert_called_once_with(
            "mong-mcp-server",
            "MCP server to generate Docker-like random names"
        )

    @patch('mong_mcp_server.server.FastMCP')
    def test_tool_registration(self, mock_fastmcp):
        """Test that the get_random_name tool is registered"""
        mock_mcp_instance = MagicMock()
        mock_fastmcp.return_value = mock_mcp_instance

        with patch('mong_mcp_server.server.FastMCP.run'):
            main()

        mock_mcp_instance.tool.assert_called_once()
        call_args = mock_mcp_instance.tool.call_args
        self.assertEqual(call_args[1]['name'], 'get_random_name')
        self.assertEqual(call_args[1]['description'], 'Generate a random name like Docker does.')

    @patch('mong_mcp_server.server.FastMCP')
    def test_server_run_called(self, mock_fastmcp):
        """Test that the server run method is called"""
        mock_mcp_instance = MagicMock()
        mock_fastmcp.return_value = mock_mcp_instance

        main()

        mock_mcp_instance.run.assert_called_once()


if __name__ == '__main__':
    unittest.main()
