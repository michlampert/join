import csv
import sys
import argparse

from src.join import join

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path_1', help='file path to first file')
    parser.add_argument('file_path_2', help='file path to second file')
    parser.add_argument('column_name', help='name of column used to join operation')
    parser.add_argument('join_type', default="inner", nargs='?', help='type of join')
    print(parser.parse_args(args))
    return parser.parse_args(args)


if __name__ == "__main__":

    args = parse_args(sys.argv[1:])

    filename1 = args.file_path_1
    filename2 = args.file_path_2
    by = args.column_name
    type = args.join_type

    with open(filename1) as file1:
        with open(filename2) as file2:
            writer = csv.writer(sys.stdout)
            for row in join(file1, file2, by, type=type): writer.writerow(row)
