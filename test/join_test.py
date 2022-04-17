import unittest
import csv

from src.join import join


class JoinTest(unittest.TestCase):

    def setUp(self):
        self.file1 = open("./test/files/file1.csv")
        self.file2 = open("./test/files/file2.csv")

    def tearDown(self):
        self.file1.close()
        self.file2.close()

    def test_inner_join(self):
        file12 = open("./test/files/file12inner.csv")
        self.assertListEqual(
            list(join(self.file1, self.file2, "id", type="inner")),
            list(csv.reader(file12)),
            "tables should be equal"
        )
        file12.close()

    def test_left_join(self):
        file12 = open("./test/files/file12left.csv")
        self.assertListEqual(
            list(join(self.file1, self.file2, "id", type="left")),
            list(csv.reader(file12)),
            "tables should be equal"
        )
        file12.close()

    def test_right_join(self):
        file12 = open("./test/files/file12right.csv")
        self.assertListEqual(
            list(join(self.file1, self.file2, "id", type="right")),
            list(csv.reader(file12)),
            "tables should be equal"
        )
        file12.close()


if __name__ == '__main__':
    unittest.main()
