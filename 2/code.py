import sys
import os


class IncorrectArgs(Exception):
    ...


class IncorrectFileExtension(Exception):
    ...


def parse_input():
    argument = sys.argv
    if(len(argument) == 2):
        filename = argument[1]
        return filename
    raise IncorrectArgs("Program expects exactly one command line argument")


def check_file(filename):
    if(not filename.endswith(".py")):
        raise IncorrectFileExtension("File should be a .py file")
    elif(not os.path.isfile(filename)):
        raise FileNotFoundError("File not found")
    return True


def read_file(filename):
    with open(filename,"r") as file:
        return file.readlines()


def count_lines(file_list):
    count = 0
    for line in file_list:
        refined_line = line.strip()
        if(not refined_line or refined_line[0]=='#'):
            continue
        else:
            count += 1
    return count

def main():        
    try:
        filename = parse_input()
        if(check_file(filename=filename)):
            file_list = read_file(filename=filename)
            count = count_lines(file_list=file_list)
            print(f"No. of lines: {count}")

    except (IncorrectArgs,IncorrectFileExtension,FileNotFoundError) as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    main()