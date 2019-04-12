# -*- coding: utf-8 -*-
import argparse
import json
import os


def validateOptions(opts):
    pass


def handleConf(options):
    if 'config-file' not in options:
        raise TypeError("No config file is supplied from command line.")

    config_file = os.path.realpath(os.path.abspath(os.path.expandvars(os.path.expanduser(options['config-file']))))

    if not os.access(config_file, os.F_OK|os.R_OK):
        raise PermissionError("The file {0} doesn't exist or you have no read permission.".format(config_file))

    with open(config_file, 'r', encoding='utf-8') as fp:
        config = json.load(fp, encoding='utf-8')

    # TODO: update options

    with open(config_file, 'w', encoding='utf-8') as fp:
        json.dump(config, fp, indent=4, ensure_ascii=False)

    return config


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
    parser.add_argument('-s', '--server', action='store', type=str, required=False, default=argparse.SUPPRESS, help='the address of your elasticesearch server.', dest='server', metavar='Server')
    parser.add_argument('-p', '--port', action='store', type=str, required=False, default=argparse.SUPPRESS, help='the port number which your elasticsearch is listening on', dest='port', metavar='Port')
    parser.add_argument('-i', '--index', action='store', type=str, required=False, default=argparse.SUPPRESS, help='the index which you want handle', dest='index', metavar='Index')
    parser.add_argument('-a', '--analyzer', action='store', type=str, required=False, default=argparse.SUPPRESS, help='the analyzer which you want to call', dest='analyzer', metavar='Analyzer')
    parser.add_argument('-d', '--data-source', action='append', type=str, default=argparse.SUPPRESS, help='data source', dest='data', metavar='DATA SOURCE')
    parser.add_argument('-c', '--config-file', action='store', type=str, required=False, default=argparse.SUPPRESS, help='%(prog)s reads configuration from your specified file if no options are supplied, and save options into this file.', dest='config-file', metavar='CONFIG-FILE')

    options = parser.parse_args(args) if len(args) else parser.parse_args()
    return vars(options)


__all__ = [
    'optParser',
    'handleConf'
]


if __name__ == '__main__':
    configure = optParser()
    print(configure)
