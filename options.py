# -*- coding: utf-8 -*-
import argparse


def validateOptions(opts):
    pass


def optParser(args=[]):
    kwargs = {
        "prog" : "runAnalyzer",
        "description" : '''Call ES Analyzer API''',
        "formatter_class" : argparse.RawDescriptionHelpFormatter,
        "argument_default" : argparse.SUPPRESS,
        "conflict_handler" : "error"
    }

    parser = argparse.ArgumentParser(**kwargs)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('-s', '--server', action='store', type=str, required=False, default='localhost', help='the address of your elasticesearch server.', dest='server', metavar='Server')
    parser.add_argument('-p', '--port', action='store', type=str, required=False, default='9220', help='the port number which your elasticsearch is listening on', dest='port', metavar='Port')
    parser.add_argument('-i', '--index', action='store', type=str, required=False, default=argparse.SUPPRESS, help='the index which you want handle', dest='index', metavar='Index')
    parser.add_argument('-a', '--analyzer', action='store', type=str, required=False, default=argparse.SUPPRESS, help='the analyzer which you want to call', dest='analyzer', metavar='Analyzer')
    parser.add_argument('-c', '--config-file', action='store', type=argparse.FileType('r', encoding='utf-8'), required=True, help='%(prog) reads configuration from your specified file.')

    options = parser.parse_args(args) if len(args) else parser.parse_args()
    return vars(options)


__all__ = [
    'optParser'
]


if __name__ == '__main__':
    configure = optParser()
    print(configure)
