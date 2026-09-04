import unittest
from unittest.mock import patch

from portscanx import cli
from portscanx.core import ScanResult


class CliTests(unittest.TestCase):
    @patch("portscanx.cli.scan", return_value=[ScanResult(80, "open", "http")])
    @patch("portscanx.cli.socket.gethostbyname", return_value="127.0.0.1")
    def test_json_output(self, _resolve, _scan):
        with patch("sys.argv", ["portscanx", "localhost", "--ports", "80", "--json"]), patch("builtins.print") as printer:
            self.assertEqual(cli.main(), 0)
        printer.assert_called_once()
        self.assertIn('"port": 80', printer.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
