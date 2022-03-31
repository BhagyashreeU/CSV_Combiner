import sys

class File:
    __filename = ""
    __cols = ""

    def write_to_stdout(self):
        with open(self.__filename, 'r') as infile:
            for lines in infile:
                if self.__cols == lines:
                    continue
                sys.stdout.write(lines.strip() + ',\"' + self.__filename.split('/')[-1] + '\"\n')
            infile.closed

    def get_cols(self):
        return self.__cols

    def set_cols(self):
        if self.__cols != "":
            return
        with open(self.__filename, 'r') as infile:
            self.__cols = infile.readline()
        infile.closed

    def __init__(self, name):
        self.__filename = name
        self.set_cols()