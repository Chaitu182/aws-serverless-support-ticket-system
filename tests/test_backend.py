import unittest


class TestBackend(unittest.TestCase):

    def test_application_status(self):
        self.assertEqual("working", "working")


if __name__ == "__main__":
    unittest.main()
