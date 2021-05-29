from setuptools import setup

setup(

    name='Markdown table generator',
    url='https://github.com/MarLisiecki/markdown_table_gen',
    author='Marcin Lisiecki',
    author_email='marcin.lisiecki@tutanota.com',
    packages=['markdown_gen'],
    install_requires=['pytest', 'pytest-cov', 'coverage'],
    version='0.1',
    license='MIT',
    description='Simple package to generate table as markdown syntax for coverage report',

)
