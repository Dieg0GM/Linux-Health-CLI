import unittest
from health import parse_meminfo


class MeminfoTests(unittest.TestCase):
    def test_kilobytes(self):
        result = parse_meminfo("MemTotal: 100 kB\nMemAvailable: 40 kB")
        self.assertEqual(result["MemTotal"], 102400)
        self.assertEqual(result["MemAvailable"], 40960)

    def test_empty(self):
        self.assertEqual(parse_meminfo(""), {})


if __name__ == "__main__":
    unittest.main()
