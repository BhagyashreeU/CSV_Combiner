import pandas as pd
import sys
import test_readfile
import unittest
import os
from csv_combiner import CSVCombiner
from io import StringIO

class CombineCSVTest(unittest.TestCase):
    # initialize all paths
    output_file = "./output_file.csv"
    csv_c_path = "./csv_combiner.py"
    accessories_path = "./test_fixtures/accessories.csv"
    clothing_test_file = "./test_fixtures/clothing.csv"
    household_cleaners_test_file = "./test_fixtures/household_cleaners.csv"
    empty_file = "./test_fixtures/empty_file.csv"
    # initialize the test output
    backup = sys.stdout
    output = open(output_file, 'w+')

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
        self.test_output = open(self.output_file, 'w+')
        sys.stdout = self.backup
        self.test_output.truncate(0)
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

    def test_no_file_paths(self):
        # run csv_combiner with no arguments
        argv = [self.csv_c_path]
        self.combiner.combine_files(argv)

        self.assertIn("Error: No file-paths input.", self.output.getvalue())

    def test_empty_files(self):
        # run csv_combiner with an empty file
        argv = [self.csv_c_path, self.empty_file]
        self.combiner.combine_files(argv)
        self.assertIn("Warning: The following file is empty: ", self.output.getvalue())

    def test_non_existent_files(self):
        # run csv_combiner with a file that doesn't exist
        argv = [self.csv_c_path, "non_existent.csv"]
        self.combiner.combine_files(argv)

        self.assertTrue("Error: File or directory not found:" in self.output.getvalue())

    def test_filename_column_added(self):
        # run csv_combiner with valid arguments
        argv = [self.csv_c_path, self.accessories_test_file, self.clothing_test_file]
        self.combiner.combine_files(argv)
        # update the test_output.csv file
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

        # check if the column exists in the produced data-frame
        with open(self.output_file) as f:
            df = pd.read_csv(f)
        self.assertIn('filename', df.columns.values)

    def test_filename_added_to_rows(self):
        # run csv_combiner with valid arguments
        argv = [self.csv_c_path, self.accessories_test_file, self.clothing_test_file]
        self.combiner.combine_files(argv)
        # update the test_output.csv file
        self.test_output.write(self.output.getvalue())
        self.test_output.close()
        # check if a filename value exists in the produced data-frame
        with open(self.output_file) as f:
            df = pd.read_csv(filepath_or_buffer=f, lineterminator='\n')
        self.assertIn('accessories.csv', df['filename'].tolist())

    def test_all_values_exist_in_combined(self):
        # run csv_combiner with valid arguments
        argv = [self.csv_c_path, self.accessories_test_file, self.clothing_test_file,
                self.household_cleaners_test_file]
        self.combiner.combine_files(argv)
        # update the test_output.csv file
        self.test_output.write(self.output.getvalue())
        self.test_output.close()
        # open all test data-frames
        acc_df = pd.read_csv(filepath_or_buffer=self.accessories_test_file, lineterminator='\n')
        clo_df = pd.read_csv(filepath_or_buffer=self.clothing_test_file, lineterminator='\n')
        hc_df = pd.read_csv(filepath_or_buffer=self.household_cleaners_test_file, lineterminator='\n')
        # ensure that all data from the fixtures exist in the resulting combined csv file
        with open(self.output_file) as f:
            combined_df = pd.read_csv(filepath_or_buffer=f, lineterminator='\n')
        self.assertEqual(len(combined_df.merge(acc_df)), len(combined_df.drop_duplicates()))
        self.assertEqual(len(combined_df.merge(clo_df)), len(combined_df.drop_duplicates()))
        self.assertEqual(len(combined_df.merge(hc_df)), len(combined_df.drop_duplicates()))