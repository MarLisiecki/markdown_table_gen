import os
from time import sleep


class MarkDownCoverageTable:
    def __init__(self, file_names: list):
        self.file_names = file_names
        self.command: list = ['coverage run -m pytest ', 'coverage report > report.txt']

    def run_tests(self):
        for element in self.file_names:
            print(self.command[0])
            os.system(self.command[0] + element)
            sleep(1)
            os.system(self.command[1])
            sleep(1)


if __name__ == '__main__':
    pass
