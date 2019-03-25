# -*- coding: utf-8 -*-
import unittest

from runAnalyzer import *


class TestMsarhan(unittest.TestCase):
    def test_access_an_nonexistent_csv(self):
        with self.assertRaises(OSError):
            process_inflection_in_a_csv_file('./data/nonexistent.csv')


    def test_access_an_existent_csv_file(self):
        process_inflection_in_a_csv_file('./data/irregular_verbs.csv')


if __name__ == '__main__':
    unittest.main()
