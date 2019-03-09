# -*- coding: utf-8 -*-
import argparse


def optParser():
    kwargs = {
        "prog" : "runAnalyzer",
        "description" : '''Call ES Analyzer API''',
        "formatter_class" : argparse.RawDescriptionHelpFormatter,
        "argument_default" : ""
    }



if __name__ == '__main__':
    optParser()
