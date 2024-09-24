"""Program to find number of lines in a python file excluding comments and blank spaces"""

import sys
import os


class IncorrectArgs(Exception):
    """Exception for incorrect number of arugments"""


class IncorrectFileExtension(Exception):
    """Exception for incorrect file extension, i.e other than .py"""


def parse_input():
    """Gets the input from command line"""
    argument = sys.argv
    if len(argument) == 2 :
        filename = argument[1]
        return filename
    raise IncorrectArgs("Program expects exactly one command line argument")


def check_file(filename):
    """Checks if the file exists and has valid extension"""
    if not filename.endswith(".py"):
        raise IncorrectFileExtension("File should be a .py file")
    if not os.path.isfile(filename):
        raise FileNotFoundError("File not found")
    return True


def read_file(filename):
    """Opens the file and returns list of lines in it"""
    with open(filename,"r",encoding="UTF-8") as file:
        return file.readlines()


def count_lines(file_list):
    """Performs the counting of lines"""
    count = 0
    for line in file_list:
        refined_line = line.strip()
        if(not refined_line or refined_line[0]=='#'):
            continue
        count += 1
    return count

def main():
    """Execution of Program"""
    try:
        filename = parse_input()
        if check_file(filename=filename):
            file_list = read_file(filename=filename)
            count = count_lines(file_list=file_list)
            print(f"No. of lines: {count}")

    except (IncorrectArgs,IncorrectFileExtension,FileNotFoundError) as exception:
        print(exception)
        sys.exit()

if __name__ == "__main__":
    main()
