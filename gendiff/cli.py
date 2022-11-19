import argparse


def get_args():
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
    args = parser.parse_args()
    file_path1 = args.first_file
    file_path2 = args.second_file
    name_format = args.format
    return name_format, file_path1, file_path2
