# -*- coding: utf-8 -*-
import unittest

from callRosette import *


class TestRosette(unittest.TestCase):
    def test_raise_an_exception_when_read_an_nonexistent_csv_file(self):
        with self.assertRaises(OSError):
            build_request_from_a_csv('./data/nonexistent.csv')



if __name__ == '__main__':
    unittest.main()
