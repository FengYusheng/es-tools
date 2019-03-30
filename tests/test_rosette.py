# -*- coding: utf-8 -*-
import unittest

from callRosette import *


class TestRosette(unittest.TestCase):
    def test_raise_an_exception_when_read_an_nonexistent_csv_file(self):
        with self.assertRaises(OSError):
            build_word_list_from_a_csv('./data/nonexistent.csv')


    def test_build_regular_verb_list(self):
        inflections = build_word_list_from_a_csv('./data/regular_verbs.csv')
        print(list(inflections))



if __name__ == '__main__':
    unittest.main()
