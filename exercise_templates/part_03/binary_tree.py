import sys

class BinaryTreeNode:
    """
    A binary tree node object.

    Arguments:
    value - The value of this node.
    left - The left child of this node.
    right - The right child of this node.
    """
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

def print_binary_tree(tree):
    """
    Print the given binary tree in order.

    Input:
    tree - A binary tree.
    """
    return

if __name__ == '__main__':
    # Call this script using:
    #   python binary_tree.py

    left_one = BinaryTreeNode(5, None, None)
    right_one = BinaryTreeNode(11, None, None)

    left_two = BinaryTreeNode(2, None, None)
    right_two = BinaryTreeNode(6, left_one, right_one)

    left_three = BinaryTreeNode(4, None, None)

    right_four = BinaryTreeNode(9, left_three, None)

    left_five = BinaryTreeNode(7, left_two, right_two)
    right_five = BinaryTreeNode(5, None,  right_four)

    root = BinaryTreeNode(2, left_five, right_five)

    print 'First tree'
    print_binary_tree(root)
    print 'Expected result: 2 7 5 6 11 2 5 9 4'

    left_one = BinaryTreeNode(1, None, None)
    right_one = BinaryTreeNode(3, None, None)

    left_two = BinaryTreeNode(5, None, None)
    right_two = BinaryTreeNode(7, None, None)

    left_three = BinaryTreeNode(2, left_one, right_one)
    right_three = BinaryTreeNode(6, left_two, right_two)

    left_four = BinaryTreeNode(9, None, None)
    right_four = BinaryTreeNode(11, None, None)

    left_five = BinaryTreeNode(13, None, None)
    right_five = BinaryTreeNode(15, None, None)

    left_six = BinaryTreeNode(10, left_four, right_four)
    right_six = BinaryTreeNode(14, left_five, right_five)

    left_seven = BinaryTreeNode(4, left_three, right_three)
    right_seven = BinaryTreeNode(12, left_six, right_six)

    root = BinaryTreeNode(8, left_seven, right_seven)

    print 'Second tree'
    print_binary_tree(root)
    print 'Expected result: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
