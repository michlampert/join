class Row(dict):
    def __init__(self, columns=[], values=[]):
        super().__init__(zip(columns, values))

    def __str__(self):
        return ",".join(self.values())

    def __add__(self, other):
        return Row(
            list(self.keys()) + list(other.keys()),
            list(self.values()) + list(other.values())
        )

    def __getitem__(self, k):
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
        assert by in self and by in other, f"{by} column does not exist"
        if self[by] == other[by] or outer:
            cols1 = list(filter(lambda col: col is not by, self.keys()))
            cols2 = list(filter(lambda col: col is not by, other.keys()))
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
