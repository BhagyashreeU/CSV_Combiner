import sys


class File:
    __filename = ""
    __cols = ""

    def __init__(self, name):
        self.__filename = name

    def define_name(self):
        return self.__filename

    def write_to_stdout(self):
        with open(self.__filename, 'r') as infile:
            for lines in infile:
                if self.__cols == lines:
                    continue
                infile.closed

    def define_cols(self):
        return self.__cols

    def store_cols(self):
        with open(self.__filename, 'r') as infile:
            self.__cols = infile.readline();
        infile.closed








