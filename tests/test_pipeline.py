# -*- coding: utf-8 -*-

import unittest

from pipeline import *


class TestPipeline(unittest.TestCase):
    def test_access_an_nonexistent_csv(self):
        with self.assertRaises(OSError):
            run('./data/nonexistent.csv')


    def test_handle_regular_verb(self):
        run('./data/regular_verbs_msarhan_report.csv')



if __name__ == '__main__':
    unittest.main()
