import sys
from file import File
import argparse

class CSVCombiner:

    def combine(self, args):
        list_of_files = [File(file.name) for file in args]

        # write input file to stdout
        col_name = ""
        sys.stdout.write(col_name.strip() + ',\"filename\"\n')

        for file in list_of_files:
            file.write_to_stdout()


def main(args):
    csv_combiner = CSVCombiner()
    csv_combiner.combine(args)
    
if __name__ == '__main__':
    parsefile = argparse.ArgumentParser(prog='csv_combiner.py',description="Merging csv files into one.")
    parsefile.add_argument('files',metavar='files',type=argparse.FileType('r'),nargs='+',help='Files to be combined into one file')
    main(parsefile.parse_args())