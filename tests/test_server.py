import unittest
from unittest.mock import patch, MagicMock
from mong_mcp_server.server import main
import mong


class TestMongMCPServer(unittest.TestCase):

    def test_get_random_name_returns_string(self):
        """Test that get_random_name returns a string"""
        with patch('mong.get_random_name') as mock_get_name:
            mock_get_name.return_value = "test_name"
            result = mong.get_random_name()
            self.assertIsInstance(result, str)
            self.assertEqual(result, "test_name")

    def test_get_random_name_called(self):
        """Test that mong.get_random_name is called"""
        with patch('mong.get_random_name') as mock_get_name:
            mock_get_name.return_value = "brave_newton"
            result = mong.get_random_name()
            mock_get_name.assert_called_once()
            self.assertEqual(result, "brave_newton")

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


class TestIntegration(unittest.TestCase):

    def test_mong_library_integration(self):
        """Test integration with the mong library"""
        result = mong.get_random_name()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        self.assertTrue('_' in result or '-' in result)

    def test_multiple_names_are_different(self):
        """Test that multiple calls return different names (probabilistically)"""
        names = set()
        for _ in range(10):
            names.add(mong.get_random_name())

        self.assertGreater(len(names), 1)


if __name__ == '__main__':
    unittest.main()
