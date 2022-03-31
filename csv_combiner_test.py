import pandas as pd
import sys
import test_readfile
import unittest
import os
from csv_combiner import CSVCombiner
from io import StringIO
import filecmp

class CombineCSVTest(unittest.TestCase):
    # initialize all paths
    output_file = "./output_file.csv"
    happy_path_expected_file = "./fixtures/happy_path_expected_file.csv"
    csv_c_path = "./csv_combiner.py"
    accessories_path = "./test_fixtures/accessories.csv"
    clothing_test_file = "./test_fixtures/clothing.csv"
    household_cleaners_test_file = "./test_fixtures/household_cleaners.csv"
    empty_file = "./test_fixtures/empty_file.csv"
    # initialize the test output
    backup = sys.stdout
    output = open(output_file, 'w+')
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
        self.test_output = open(self.output_file, 'w+')
        sys.stdout = self.backup
        self.test_output.truncate(0)
        self.test_output.write(self.output.getvalue())
        self.test_output.close()

    def test_happy_path(self):
        # run csv_combiner with one 
        file_paths = [self.clothing_test_file, self.accessories_path]
        self.csv_combiner.combine(file_paths)
        self.assertIn("True", filecmp.cmp(output_file, happy_path_expected_file, shallow=False))