# -*- coding: utf-8 -*-
import unittest

from runAnalyzer import *


class TestRosette(unittest.TestCase):
    def test_rosette(self):
        process_inflection_in_a_csv_file('./data/regular_verbs.csv', 'rosette')




if __name__ == '__main__':
    unittest.main()
