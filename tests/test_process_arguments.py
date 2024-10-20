import unittest
from yaml2cmd.yaml2cmd import process_arguments


class TestProcessArguments(unittest.TestCase):

    def test_process_arguments(self):
        processed_args = process_arguments("test", ["a", "b", "c"])
        self.assertEqual("test a b c", processed_args)


unittest.main()
