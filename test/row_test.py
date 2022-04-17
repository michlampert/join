import unittest

from src.row import Row, empty


class RowTest(unittest.TestCase):
    def test_join(self):
        row1 = Row(["id", "c1"], ["1", "a"])
        row2 = Row(["id", "c2"], ["1", "b"])
        row3, _ = row1.join(row2, "id")
        self.assertEqual(
            row3,
            Row(["id", "c1", "c2"], ["1", "a", "b"]),
            "rows should be equal"
        )

    def test_outer_join(self):
        row1 = Row(["id", "c1"], ["1", "a"])
        row2 = empty(["id", "c2"])
        row3, _ = row1.join(row2, "id", outer=True)
        self.assertEqual(
            row3,
            Row(["id", "c1", "c2"], ["1", "a", ""]),
            "rows should be equal"
        )

    def test_duplicated_columns(self):
        row1 = Row(["id", "c1"], ["1", "a"])
        row2 = Row(["id", "c1"], ["1", "b"])
        row3, _ = row1.join(row2, "id")
        self.assertEqual(
            row3,
            Row(["id", "c1_1", "c1_2"], ["1", "a", "b"]),
            "rows should be equal"
        )


if __name__ == '__main__':
    unittest.main()
