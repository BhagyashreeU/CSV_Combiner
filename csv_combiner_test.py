import sys
import unittest
import os
from csv_combiner import CSVCombiner
from io import StringIO
import filecmp
import time


class CSVCombinerTest(unittest.TestCase):
    output_file = "./output_file.csv"

    happy_path_expected_file = "./fixtures/happy_path_expected_file.csv"
    accessories_path = "./fixtures/test-accessories.csv"
    clothing_test_file = "./fixtures/test-clothing.csv"

    # when testing locally, I used the below paths for files > 4 GB. The implementation code
    # didn't fail with memory issues but the test did. So the test which uses below variables
    # is commented
    happy_path_expected_large_file = "./fixtures/happy_path_expected_file_large.csv"
    accessories_path_large = "./fixtures/test-accessories-large.csv"
    clothing_test_file_large = "./fixtures/test-clothing-large.csv"

    # initialize the test output
    backup = sys.stdout
    test_output = open(output_file, 'w+')
    csv_combiner = CSVCombiner()

    @classmethod
    def setUpClass(cls):
        # redirect the output to ./test_output.csv
        sys.stdout = cls.test_output

    def setUp(self):
        # setup
        self.output = StringIO()
        sys.stdout = self.output
        self.test_output = open(self.output_file, 'w+')

    def tearDown(self):
        self.test_output.close()
        sys.stdout = self.backup

    def test_happy_path(self):
        # run csv_combiner with two files
        files = [open(self.accessories_path, 'r'), open(self.clothing_test_file, 'r')]
        self.csv_combiner.combine(files)
        self.close_files(files)
        self.test_output.truncate(0)
        self.test_output.write(self.output.getvalue())
        self.test_output.close()
        self.assertEqual(True, filecmp.cmp(self.output_file, self.happy_path_expected_file, shallow=False))

    # def test_happy_path_large(self):
    #     # run csv_combiner with two very large files
    #     # tested for files > 4 GB, the implementation didn't fail for memory issues but test failed with memory issues.
    #     # So keeping this test commented
    #     files = [open(self.accessories_path_large, 'r'), open(self.clothing_test_file_large, 'r')]
    #     self.csv_combiner.combine(files)
    #     self.close_files(files)
    #     self.test_output.truncate(0)
    #     self.test_output.write(self.output.getvalue())
    #     self.test_output.close()
    #     self.assertEqual(True, filecmp.cmp(self.output_file, self.happy_path_expected_file_large, shallow=False))

    def close_files(self, files):
        for file in files:
            file.close()


if __name__ == "__main__":
    unittest.main()
