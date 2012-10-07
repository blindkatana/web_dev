import sys


"""
Determine whether the given year is a leap year or not.

Input:
year - The year.

Return:
True if the year is a leap year.
"""
def is_leap_year(year):
    return

if __name__ == '__main__':
    # sys.argv is a list of the arguments to the python call. The first argument
    # should be the name of the file (leap_year.py) and the other arguments
    # should be the flags and inputs for that file.
    script_name = sys.argv[0] # Unnecessary line.
    args = sys.argv[1:end]

    # Need to cast the argument as an integer.
    print is_leap_year(int(args[0]))
