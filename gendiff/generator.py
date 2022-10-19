import argparse


def generate_reference():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     usage='%(prog)s [-h]'
                                     ' first_file second_file',
                                     description='Compares two'
                                     ' configuration files'
                                     ' and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.parse_args()
