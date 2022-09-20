import sys


def opening_and_closing_files():
    f = open("think_different.txt")  # details: https://docs.python.org/3/library/functions.html#open
    quote = f.read()
    print(f"{quote = }")
    # try and read again
    quote_again = f.read()
    print(f"{quote_again = }")
    # don't forget!
    f.close()


def reading_file_contents():
    with open("think_different.txt") as f:
        # read everything
        print(f"{f.read()[:30]}...")

    print(f"{f = }")
    print(f"{f.closed = }")
    # print(f"{f.read() = }") # raises ValueError: I/O operation on closed file

    with open("think_different.txt") as f:
        # read one line at a time; up to the \n
        print(f"{ f.readline() = }")

    with open("think_different.txt") as f:
        # list of all lines
        print(f"{ f.readlines() = }")


def iterating_over_file_contents(): #prints all in a file
    with open("think_different.txt") as f:
        for row in f:
            print(row.strip()) #strip before prinintg to remove spaces between lines

def reading_wagata():
    with open("wagata.txt", encoding="utf-8") as f:
        for row in f:
            print(row)


def print_number_of_rows(lines=10):
    with open("paradoxical.txt") as f:
        lines_read = f.readlines()[:lines]
        print(lines_read)
        print(len(lines_read))


def navigating_files():
    with open("butterfly.txt") as f:
        # first let's read everything
        print(f"{f.read() = }")
        # try and read again... nothing
        print(f"{f.read() = }")
        # where are we?
        print(f"{f.tell() = }")
        # let's go back to the beginning
        print(f"{f.seek(0) = }")
        # ten steps forward....
        print(f"{f.seek(10) = }")
        # perfect!
        print(f"{f.read() = }")


def working_with_paths():
    import pathlib
    my_path = pathlib.Path(".")  # bash: the current directory
    print(f"{type(my_path)}")  # what is the type
    print(f"{my_path.owner() = }")
    print(f"{my_path.parent = }")
    print(f"{my_path.name = }")
    print(f"{my_path.parent.absolute() = }")
    print(f"{my_path.parents = }")
    file_path = my_path / 'our_deepest_fear.txt.gz'  # paths works with the / operator
    print(f"{my_path / 'our_deepest_fear.txt.gz' = }")
    print(f"{file_path.absolute() = }")
    print(f"{file_path.name = }")
    print(f"{file_path.suffix = }")
    print(f"{file_path.suffixes = }")
    print(f"{file_path.stem = }")


def testing_paths():
    import pathlib
    my_path = pathlib.Path("..")  # the parent directory
    print(f"{my_path.exists() = }")
    print(f"{my_path.is_dir() = }")
    print(f"{my_path.is_file() = }")
    print(f"{my_path.is_absolute() = }")
    print(f"{my_path.is_relative_to('/Users/paulkorir/') = }")
    print(f"{my_path.is_relative_to('.') = }")


def useful_path_operations():
    import pathlib
    my_path = pathlib.Path("/Users/paulkorir/PycharmProjects/code-fastfoundations/day2/dir1/dir3/dir4/einstein.txt")
    with my_path.open() as f:
        print(f.read())
    my_path = pathlib.Path("~/PycharmProjects/code-fastfoundations/day2/dir1/dir3/dir4/einstein.txt")  # ~ = user dir
    # with my_path.open() as f: # raises an exception
    #     print(f.read())
    with my_path.expanduser().open() as f:  # need to expand user first
        print(f.read())
    my_path = pathlib.Path("/Users/paulkorir/PycharmProjects/code-fastfoundations/day2")
    print(f"{my_path.glob('*') = }")  # globbing; just like on the bash terminal
    print(f"{'GLOBBING'}")
    for path_object in my_path.glob('*'):
        print(f"\t* {path_object.name:<30} ==> {path_object.parent}")
    print(f"{'GLOBBING & SORTING'}")
    for python_modules in sorted(my_path.glob('*.py')):  # sortable!
        print(f"\t* {python_modules.name}")
    print(f"{'RECURSIVE GLOBBING'}")
    for path_object in my_path.rglob('**/*'):  # recursive globbing
        print(f"\t* {path_object.name:<30} ==> {path_object.parent}")


def reading_socrates():
    import pathlib
    my_path = pathlib.Path("day2/dir1/dir2/socrates.txt")
    with my_path.open() as f:
        print()


def read_hidden():
    import pathlib
    my_path = pathlib.Path("~/") #show hidden files
    for fn in my_path.expanduser().glob(".*"):
        print(fn)


def main():
    # opening_and_closing_files()
    # reading_file_contents()
    # iterating_over_file_contents()
    # reading_wagata()
    # print_number_of_rows()
    # navigating_files()
    # # working_with_paths()
    # # testing_paths()
    # useful_path_operations()
    # reading_socrates()
    read_hidden()
    return 0


if __name__ == '__main__':
    sys.exit(main())

