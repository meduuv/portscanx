import unittest

from portscanx.core import parse_ports


class ParsePortsTests(unittest.TestCase):
    def test_ranges_and_values_are_sorted_and_unique(self):
        self.assertEqual(parse_ports("80,22,80,443-445"), [22, 80, 443, 444, 445])

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            parse_ports("100-10")

    def test_out_of_range_port(self):
        with self.assertRaises(ValueError):
            parse_ports("65536")


if __name__ == "__main__":
    unittest.main()
