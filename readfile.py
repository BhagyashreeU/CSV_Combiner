import sys

class CombineFiles:
    __name = ""
    __lines = ""
    __cols = ""

    def __init__(self,name):
        self.__name = name
    def define_name(self):
        return self.__name
    
    def process_csv_file(self):
        with open(self.__name,'r') as infile:
            for lines in infile:
                if self.__cols == lines:
                    continue
                else:
                    sys.stdout.write(lines.strip() + ',\"' + self.__name.split('/')[-1] + '\"\n')
                infile.closed
    def define_cols(self):
        return self.__cols

    def update_cols(self):
        with open(self.__name,'r') as infile:
            self.__cols = infile.readline();
        infile.closed








