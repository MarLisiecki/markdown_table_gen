# Table generator with markdown syntax
[![CircleCI](https://circleci.com/gh/MarLisiecki/markdown_table_gen.svg?style=shield)](https://circleci.com/gh/MarLisiecki/markodwn_table_gen)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub version](https://badge.fury.io/gh/MarLisiecki%2Fmarkdown_table_gen.svg)](https://badge.fury.io/gh/MarLisiecki%2Fmarkdown_table_gen)

##  Created by:
[![N|Solid](https://i.imgur.com/zk7PUsqm.jpg)](https://nodesource.com/products/nsolid)


Simple package which allows you to generate tables from CSV or
for the report with information on coverage (pytest) if you have tests for your scripts.

## Preparations

- open your terminal and write (remeber to activate your venv)
```console
pip install git+https://github.com/MarLisiecki/markdown_table_gen.git
```
- it will automatically install all requirements
- now you can use lib

## Requirements
- Python 3.x
- look at the requirements(it will be automatically installed)

## Usage
You have some code:
```py
def add_num(a,b):
    return a + b
```
And some tests:
```py
def test_add_num():
    assert add_num(2, 2) == 4
```
All you have to do is just:
```py
mdct = MarkDownCoverageTable(['test_add.py']) # put into a list all test files you want to run
mdct.run_tests()                              # run your tests with a function
mdct.create_csv_from_txt()                    # convert report from TXT to CSV  
mdct.create_markdown_file()                   # generate markdown file with proper syntax
```
As an output you will see new file named Report.md, which contains reports:
```md
|    Name   |   Stmts   |    Miss   |   Cover   |
|----------:|----------:|----------:|----------:|
|   add.py  |     8     |     4     |    50%    |
|test_add.py|     3     |     0     |    100%   |
```
Now you can eg. put your coverage report into README.md file or just push it into your repository
Also you can generate your own table from CSV all you have to do is:
```py
mdtg = MarkDownTableGenerator('custom.csv', title = 'Custom') # title is optional: default is Table.md
mdtg.generate_markdown_file()                                 # generate markdown file with proper syntax