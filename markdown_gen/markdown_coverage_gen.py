import os
from time import sleep

from markdown_gen.markdown_gen import *


class MarkDownCoverageTable:
    def __init__(self, file_paths: list):
        """
        Initial function

        Args:
            file_paths: File paths for tests with name
            Examples:
                If file is in another directory:
                mdct = MarkDownCoverageTable(['ttt/test_add.py'])
                If file is in root directory:
                mdct = MarkDownCoverageTable(['test_add.py'])

        """
        self.file_names = file_paths
        self.command: list = ['coverage run -m pytest ', 'coverage report > report.txt']

    def run_tests(self):
        """
        Function which automatically run test end generate report.txt

        """
        for element in self.file_names:
            print(self.command[0])
            os.system(self.command[0] + element)
            sleep(1)
            os.system(self.command[1])
            sleep(1)

    def prepare_txt(self):
        """
        Functon which prerare text file and delete site-packages from report

        Returns:
            list: Return list with report
        """
        with open('report.txt', "r+") as file:
            content = file.readlines()
            output = list()
            for element in content:
                if 'site-packages' in element:
                    pass
                elif '---' in element:
                    pass
                elif 'TOTAL' in element:
                    pass
                else:
                    output.append(element.split(','))
            return output

    def create_csv_from_txt(self):
        """
        Function which genereate CSV file from properly prepared text file

        """
        input = self.prepare_txt()
        with open('report.csv', 'w') as file:
            for element in input:
                for single in element:
                    single = ';'.join(single.split())
                    file.write(single + '\n')

    def create_markdown_file(self):
        """
        Function which generate markdown file with coverage report

        """
        mdtg = MarkDownTableGenerator('report.csv', title='Report')
        mdtg.generate_markdown_file()


if __name__ == '__main__':
    pass
