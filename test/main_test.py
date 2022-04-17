import unittest
import os
import csv


class MainTest(unittest.TestCase):

    def setUp(self):
        os.system("mkdir tmp")

    def tearDown(self):
        os.system("rm tmp/output.csv")
        os.system("rmdir tmp")

    def test_main_inner(self):
        os.system(
            "python3 main.py test/files/file1.csv test/files/file2.csv id > tmp/output.csv")
        output = open("./tmp/output.csv")
        file12 = open("./test/files/file12inner.csv")
        self.assertListEqual(
            list(csv.reader(file12)),
            list(csv.reader(output))
        )

    def test_main_left(self):
        os.system(
            "python3 main.py test/files/file1.csv test/files/file2.csv id left > tmp/output.csv")
        output = open("./tmp/output.csv")
        file12 = open("./test/files/file12left.csv")
        self.assertListEqual(
            list(csv.reader(file12)),
            list(csv.reader(output))
        )

    def test_main_right(self):
        os.system(
            "python3 main.py test/files/file1.csv test/files/file2.csv id right > tmp/output.csv")
        output = open("./tmp/output.csv")
        file12 = open("./test/files/file12right.csv")
        self.assertListEqual(
            list(csv.reader(file12)),
            list(csv.reader(output))
        )


if __name__ == '__main__':
    unittest.main()
