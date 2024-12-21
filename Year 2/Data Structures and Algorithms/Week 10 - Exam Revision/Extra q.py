#####################################################
class BinaryTree:
    def __init__(new_tree, v):
        new_tree.value = v
        new_tree.left_child = None
        new_tree.right_child = None

    def __str__(root):
        s = str(root.value)
        s += " <"
        child_strings = []
        left = root.left_child
        right = root.right_child
        if left != None or right != None:
            child_strings.append(str(left))
            child_strings.append(str(right))
        s += ", ".join(child_strings)
        s += ">"
        return s

    def __repr__(root):
        return str(root)


class Tree:
    def __init__(new_tree, v):
        new_tree.value = v
        new_tree.children = []

    def __str__(root):
        s = str(root.value)
        s += " <"
        child_strings = []
        for child in root.children:
            child_strings.append(str(child))
        s += ", ".join(child_strings)
        s += ">"
        return s

    def __repr__(root):
        return str(root)


#####################################################


x = 17


def run(t):
    if isinstance(t.value, int):  # loop
        for i in range(t.value):
            for child in t.children:
                run(child)
    if t.value == "inc":  # Other instructions
        x = x + 1
    elif t.value == "dec":
        x = x - 1
    elif t.value == "dbl":
        x = x * 2
    elif t.value == "hlf":
        x = x // 2


def has_dup(t):
    "to do"


def xhash(s):
    """
    Calculates the hash of a string by converting each character to a scrambled number
    and mixing it with the next character's value using XOR.

    Args:
        s (str): The input string.

    Returns:
        int: The calculated hash value.
    """
    if not s:
        return 0  # Handle empty string

    x = ord(s[0]) * 43  # Initialize x with the scrambled value of the first character
    for char in s[1:]:
        y = ord(char) * 43  # Scramble the next character
        x = x ^ y  # Mix x with the scrambled value of the next character using XOR

    return x
