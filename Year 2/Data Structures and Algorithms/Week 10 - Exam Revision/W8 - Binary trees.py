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


def follow(t, s):
    current = t
    for step in s:
        if current is None:
            break
        if step == "left":
            current = current.left_child
        elif step == "right":
            current = current.right_child
    return current.value if current else None

def in_range(t, low, high):
    "to do"


def in_range_v2(t, low, high):
    "to do"


def ctree(x, n):
    "to do"