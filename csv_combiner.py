import sys
from file import File
import argparse


class CSVCombiner:
    def combine(self, files):
        list_of_files = [File(file.name) for file in files]

        # write input file to stdout
        is_cols_header_written = False
        for file in list_of_files:
            if not is_cols_header_written:
                is_cols_header_written = True
                sys.stdout.write(file.get_cols().strip() + ',\"' + 'filename' + '\"\n')
            file.write_to_stdout()


def main(args):
    csv_combiner = CSVCombiner()
    csv_combiner.combine(args.files)


if __name__ == '__main__':
    parsefile = argparse.ArgumentParser(prog='csv_combiner.py', description="Merging csv files into one.")
    parsefile.add_argument('files', metavar='files', type=argparse.FileType('r'), nargs='+',
                           help='Files to be combined into one file')
    main(parsefile.parse_args())
