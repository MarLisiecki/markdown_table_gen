import os
from pathlib import Path

from markdown_gen.markdown_gen import MarkDownTableGenerator
from tests.test_sup import ConstForTests


def test_create_header():
    """
    Testing the creation of header with proper syntax.

    """
    mdtg = MarkDownTableGenerator('TEST.csv')
    created_header = mdtg.create_header()
    assert created_header == '|TEST1|TEST2|TEST3|TEST4|TEST5|'


def test_space_header():
    """
    Testing the creation of gap in syntax which bolds header with proper syntax.

    """
    mdtg = MarkDownTableGenerator('TEST.csv')
    space_header = mdtg.space_header()
    assert space_header == '|----:|----:|----:|----:|----:|'


def test_create_content():
    """
     Testing the creation of content from CSV's body with proper syntax.

     """
    mdtg = MarkDownTableGenerator('TEST.csv')
    content = mdtg.create_content()
    assert content == ConstForTests.CONST_FOR_CONTENT_TEST


def test_max_size():
    """
     Testing the creation of content from CSV's body with proper syntax.

     """
    mdtg = MarkDownTableGenerator('TEST.csv')
    max_size = mdtg.max_size()
    assert max_size == 5


def test_create_header_list():
    """
     Testing the creation of a list with header's elements.

     """
    mdtg = MarkDownTableGenerator('TEST.csv')
    header = mdtg.create_header_list()
    assert header == ['TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5\n']


def test_create_full_table():
    """
       Testing the creation of table (bold header + body) with proper syntax.

       """
    mdtg = MarkDownTableGenerator('TEST.csv')
    table_syntax = mdtg.create_full_table()
    assert table_syntax == ConstForTests.CONST_FOR_TABLE_TEST


def test_generate_markdown():
    """
    Testing the creation of markdown file.

    """
    mdtg = MarkDownTableGenerator('TEST.csv', title ='Table')
    mdtg.generate_markdown_file()
    assert os.path.exists(os.path.join(Path(__file__).parent.parent,'Table.md')) == True
