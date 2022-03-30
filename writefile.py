import sys
from readfile import CombineFiles
import argparse

parsefile = argparse.ArgumentParser(prog='readfile.py',description="Merging csv files into one.")
parsefile.add_argument('files',metavar='files',type=argparse.FileType('r'),nargs='+',help='Files to be combined into one file')

args = parsefile.parse_args()


list_of_files = [CombineFiles(file.name) for file in args.files]

# write input file to stdout
col_name = ""
sys.stdout.write(col_name.strip() + ',\"filename\"\n')

for file in list_of_files:
    file.process_csv_file()


