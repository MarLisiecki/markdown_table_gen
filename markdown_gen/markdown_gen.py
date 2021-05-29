from pathlib import Path


class MarkDownTableGenerator:
    def get_project_root(self) -> Path:
        """
        Function which return a path for the project, which will help to generate markdown output file.

        Returns:
            object: Path
        """
        return Path(__file__).parent.parent

    def __init__(self, path_to_file: str, **kwargs):
        """
        Initialize object with path to CSV file and optional title for markdown output file as kwargs.

        Args:
            path_to_file(str): Path to file which will be used.
            **kwargs: Arbitrary keyword arguments.
        """
        self.path_to_file = path_to_file
        self.title = kwargs.get('title', 'Table')

    def create_header_list(self):
        """
        Function which get header from file and return list with elements of header.

        Returns:
            List
        """
        with open(self.path_to_file) as file:
            header_from_file = (file.readline()).split(';')
            return header_from_file

    def max_size(self):
        """
        Function which get the longest element in CSV file, it will be used to
        format output table properly.

        Returns:
            int: if find the longest element in whole CSV file.
        """
        with open(self.path_to_file) as file:
            all_content = list()
            content = file.readlines()
            for element in content:
                element = element.rstrip('\n').split(';')
                for item in element:
                    all_content.append(item)
            return len(max(all_content, key=len))

    def create_header(self):
        """
        Function which create header with proper syntax for markdown file.

        Returns:
            str: Return header for the file.
        """
        header = self.create_header_list()
        markdown_header = str()
        for element in header:
            markdown_header += ('|' + element.center(self.max_size()))
        markdown_header = markdown_header.replace('\n', '')
        markdown_header += '|'
        return markdown_header

    def space_header(self):
        """
        Function which create syntax for bold header.

        Returns:
            str:  Syntax to make header bold.
        """
        header = self.create_header()
        space_syntax = str()
        for index, letter in enumerate(header):
            if letter != '|' and header[index + 1] != '|':
                letter = '-'
            if letter != '|' and header[index + 1] == '|':
                letter = ':'
            space_syntax += letter
        return space_syntax

    def create_content(self):
        """
        Function which convert the body of CSV file into markdown's table syntax.


        Returns:
            str: String contains all content from body as markdown syntax.
        """
        content_syntax = str()
        with open(self.path_to_file) as file:
            content = file.readlines()
            del (content[0])
            for element in content:
                line_content = str()
                element = element.rstrip('\n')
                element = element.split(';')
                for item in element:
                    line_content += '|' + item.center(self.max_size())
                line_content += '|' + '\n'
                content_syntax += line_content
            return content_syntax

    def create_full_table(self):
        """
        Function which finally get header, spacing(bold) and content strings and combines it.

        Returns:
            str: String contains bold header and body as markdown syntax.
        """
        full_table_syntax = str()
        header = self.create_header()
        full_table_syntax += header + '\n'
        separation = self.space_header()
        full_table_syntax += separation + '\n'
        content = self.create_content()
        full_table_syntax += content
        return full_table_syntax

    def generate_markdown_file(self):
        """
        Function which create markdown file which contains table with proper syntax.

        """
        table = self.create_full_table()

        with open(str(self.get_project_root().parent.parent.parent) + "\\" + self.title + '.md', 'w') as file:
            file.write(table)


if __name__ == '__main__':
    pass
