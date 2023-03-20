
import unittest
import bashdown

class TestCliArgParser(unittest.TestCase):

    def test_parser(self):
        parser = bashdown.cli_arg_parser(['myfilename'])
        self.assertTrue(parser.filename)


if __name__ == "__main__":
    unittest.main()
