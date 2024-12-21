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


def min(t):
    # base case, if tree is empty
    if t is None:
        return None
    current = t
    while current.left_child is not None:
        current = current.left_child
    return current.value

# Find the successor of the root t in the tree
def succ(t):
    # if t is none, or right child is none, return None
    if t is None or t.right_child is None:
        return None
    # return def again and traverse
    return min(t.right_child)

# Copy code from def in_range_v2 from W8, given a binary tree,
# check if it is an actual binary tree, if so return true
def check(t):
    return