import csv
import logging
import sys
import argparse

from src.join import join


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path_1', help='file path to first file')
    parser.add_argument('file_path_2', help='file path to second file')
    parser.add_argument(
        'column_name', help='name of column used to join operation')
    parser.add_argument('join_type', default="inner",
                        nargs='?', help='type of join')
    return parser.parse_args(args)


if __name__ == "__main__":

    args = parse_args(sys.argv[1:])

    filename1 = args.file_path_1
    filename2 = args.file_path_2
    by = args.column_name
    type = args.join_type

    file1 = open(filename1)
    file2 = open(filename2)

    try:
        writer = csv.writer(sys.stdout)
        for row in join(file1, file2, by, type=type):
            writer.writerow(row)
    except Exception as e:
        logging.error(e)
    finally:
        file1.close()
        file2.close()
