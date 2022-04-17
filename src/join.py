import csv
from ctypes import sizeof
import logging

from src.row import Row, empty


def join(file1, file2, by, type="inner", lsuffix="_1", rsuffix="_2"):
    '''
    Simple implementation of nested loop join operation, which enables to join two tables in `O(n·k)` time complexity.
    Rows are loaded one by one, so size of input files can be bigger than avaible memory space.
    '''

    csv_reader1 = csv.reader(file1)
    csv_reader2 = csv.reader(file2)

    # Names of columns can be read by loading first line in each file
    columns1 = next(csv_reader1)
    columns2 = next(csv_reader2)

    # Column names. Will be useful to change order of columns if type=="right"
    columns = empty(columns1).join(empty(columns2), by)[0].columns()
    yield columns

    left, right = get_type(type)

    # Right join can be performed as left join with changed tables order
    if right:
        csv_reader1, csv_reader2 = csv_reader2, csv_reader1
        file1, file2 = file2, file1
        columns1, columns2 = columns2, columns1
        lsuffix, rsuffix = rsuffix, lsuffix

    for line1 in csv_reader1:
        check = False

        # After each iteration on second table, position in file has to be reverted
        file2.seek(0)
        
        for line2 in csv_reader2:
            new_row, success = Row(columns1, line1).join(
                Row(columns2, line2), by, lsuffix=lsuffix, rsuffix=rsuffix)
            if success:
                check = True
                yield new_row[columns]

        # If function perform outer join, each row have to occur in new table at least once
        if (left or right) and not check:
            new_row, success = Row(columns1, line1).join(
                empty(columns2), by, outer=True, lsuffix=lsuffix, rsuffix=rsuffix)
            yield new_row[columns]


def get_type(type):
    if type == "inner":
        return False, False
    elif type == "left":
        return True, False
    elif type == "right":
        return False, True
    else:
        logging.warning(
            f"Argument {type} as join_type is incorrect. 'inner' will be used instead")
        return False, False
