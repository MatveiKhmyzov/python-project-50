import argparse


def parse_arguments(args):
    parser = argparse.ArgumentParser(prog='gendiff',
                                     usage='%(prog)s [-h]'
                                           ' first_file second_file',
                                     description='Compares two'
                                                 ' configuration files'
                                                 ' and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default="stylish",
                        help='set format of output: (default: stylish)')
    return parser.parse_args(args)


def get_args(argv):
    args = parse_arguments(argv)
    file_path1 = args.first_file
    file_path2 = args.second_file
    name_format = args.format
    return file_path1, file_path2, name_format
