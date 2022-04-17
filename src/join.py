import csv
import logging
import sys
import os

from src.row import Row, empty

def join(file1, file2, by, type = "inner", lsuffix = "_1", rsuffix = "_2"):
    csv_reader1 = csv.reader(file1)
    columns1 = next(csv_reader1)
    csv_reader2 = csv.reader(file2)
    columns2 = next(csv_reader2)
    columns = empty(columns1).join(empty(columns2), by)[0].columns()
    yield columns

    left, right = get_type(type)
    
    if right:
        csv_reader1, csv_reader2 = csv_reader2, csv_reader1
        file1, file2 = file2, file1
        columns1, columns2 = columns2, columns1
        lsuffix, rsuffix = rsuffix, lsuffix

    for line1 in csv_reader1:
        check = False
        file2.seek(0)
        for line2 in csv_reader2:
            new_row, success = Row(columns1, line1).join(Row(columns2, line2), by, lsuffix=lsuffix, rsuffix=rsuffix)
            if success:
                check = True
                yield new_row[columns]
        if (left or right) and not check:
            new_row, success = Row(columns1, line1).join(empty(columns2), by, outer=True, lsuffix=lsuffix, rsuffix=rsuffix)
            yield new_row[columns]

def get_type(type):
    if type == "inner":
        return False, False
    elif type == "left":
        return True, False
    elif type == "right":
        return False, True
    else:
        logging.warning(f"Argument {type} as join_type is incorrect. 'inner' will be used instead")
        return False, False