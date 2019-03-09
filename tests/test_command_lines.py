# -*- coding: utf-8 -*-
import unittest

from runAnalyzer import *


class TestCommandLines(unittest.TestCase):
    def test_default_options(self):
        options = optParser()
        self.assertEqual(options['server'], 'localhost')



if __name__ == '__main__':
    unittest.main()
