import sys


"""
Find the sum of the squares of the two largest numbers.

Input:
x - The first number.
y - The second number.
z - The third number.

Return:
The sum of the squares of the two largest numbers.
"""
def calculate(x, y, z):
    return

if __name__ == '__main__':
    # sys.argv is a list of the arguments to the python call. The first argument
    # should be the name of the file (arithmetic.py) and the other arguments
    # should be the flags and inputs for that file.
    script_name = sys.argv[0] # Unnecessary line.
    args = sys.argv[1:end]

    # Need to cast the argument as an integer.
    print calculate(int(args[0]), int(args[1]), int(args[2]))
