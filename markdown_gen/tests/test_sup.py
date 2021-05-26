
class ConstForTests():

    CONST_FOR_CONTENT_TEST = str()
    CONST_FOR_TABLE_TEST = str()

    with open ('test_strings_content.txt') as test_string:
        test_content = test_string.readlines()
        for element in test_content:
            CONST_FOR_CONTENT_TEST += element

    with open ('test_string_table_syntax.txt') as test_string:
        test_content = test_string.readlines()
        for element in test_content:
            CONST_FOR_TABLE_TEST += element