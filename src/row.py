class Row(dict):
    '''
    Class used to process lines from .csv files.

    It is a subclass of standard dictionary, so it keep order of entries.
    '''

    def __init__(self, columns=[], values=[]):
        super().__init__(zip(columns, values))

    def __str__(self):
        return ",".join(self.values())

    def __add__(self, other):
        return Row(
            list(self.keys()) + list(other.keys()),
            list(self.values()) + list(other.values())
        )

    def __eq__(self, other):
        if type(other) == Row:
            return list(self.keys()) == list(other.keys()) and list(self.values()) == list(other.values())
        return super().__eq__(other)

    def __getitem__(self, k):
        '''
        Extended implementation allows to get some subset of values, like in `pandas.Dataframe`. In particular, it can be used to change columns order.
        '''
        if type(k) is list:
            return list(map(lambda id: self[id], k))
        return super().__getitem__(k)

    def add_suffix(self, columns=None, suffix="_2"):
        if columns == None:
            columns = self.keys()
        return Row([column + (suffix if column in columns else "") for column in self.keys()], self.values())

    def columns(self):
        return list(self.keys())

    def join(self, other, by, outer=False, lsuffix="_1", rsuffix="_2"):
        '''
        Enables joining two rows by one column

        `other` - other `Row` object

        `by` - name of column by which two rows will be joined

        `outer` - used to create incomplete rows for [left|right] outer joins

        `lsuffix`, `rsuffix` - suffixes added in case of column name colision

        return `(True, new_row)` if operation can be performed or `(False, None)` in the otherwise.
        '''
        assert by in self and by in other, f"Column {by} does not exist"
        if self[by] == other[by] or outer:
            cols1 = list(filter(lambda col: col != by, self.keys()))
            cols2 = list(filter(lambda col: col != by, other.keys()))
            duplicates = set(cols1) & set(cols2)
            row = (
                Row([by], [self[by] or other[by]])
                + Row(cols1, self[cols1]).add_suffix(duplicates, lsuffix)
                + Row(cols2, other[cols2]).add_suffix(duplicates, rsuffix)
            )
            return row, True
        else:
            return None, False


def empty(columns=[], default=""):
    return Row(columns, [default] * len(columns))
