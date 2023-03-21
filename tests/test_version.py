
import unittest
import bashdown

class TestVersion(unittest.TestCase):

    def test_version(self):
        self.assertRegex(bashdown.__version__, r'^[0-9]*\.[0-9]*\.[0-9]*$')


if __name__ == "__main__":
    unittest.main()
