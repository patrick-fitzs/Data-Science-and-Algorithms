#####################################################
class BinaryTree:
    def __init__(new_tree, v):
        # Initialize a binary tree node with a given value `v`.
        new_tree.value = v  # Assign the provided value to the node.
        new_tree.left_child = None  # Initially, the left child is set to None.
        new_tree.right_child = None  # Initially, the right child is set to None.

    def __str__(root):
        # Define the string representation of the binary tree.
        s = str(root.value)  # Start with the value of the current node.
        s += " <"  # Add an opening angle bracket for child nodes.
        child_strings = []  # Initialize an empty list to store child node strings.
        # Get references to the left and right child nodes.
        left = root.left_child
        right = root.right_child
        # Add string representations of child nodes if they exist.
        if left is not None or right is not None:
            child_strings.append(str(left))  # Add left child to the list.
            child_strings.append(str(right))  # Add right child to the list.
        s += ", ".join(child_strings)  # Join child strings with commas.
        s += ">"  # Add a closing angle bracket for child nodes.
        return s  # Return the complete string representation.

    def __repr__(root):
        # Define the representation of the binary tree (same as __str__).
        return str(root)  # Use the string representation.

class Tree:
    def __init__(new_tree, v):
        # Initialize an n-ary tree node with a given value `v`.
        new_tree.value = v  # Assign the provided value to the node.
        new_tree.children = []  # Initialize an empty list for child nodes.

    def __str__(root):
        # Define the string representation of the n-ary tree.
        s = str(root.value)  # Start with the value of the current node.
        s += " <"  # Add an opening angle bracket for child nodes.
        child_strings = []  # Initialize an empty list to store child node strings.
        # Loop through all child nodes.
        for child in root.children:
            child_strings.append(str(child))  # Add each child's string representation to the list.
        s += ", ".join(child_strings)  # Join child strings with commas.
        s += ">"  # Add a closing angle bracket for child nodes.
        return s  # Return the complete string representation.

    def __repr__(root):
        # Define the representation of the n-ary tree (same as __str__).
        return str(root)  # Use the string representation.
#####################################################

def follow(t, s):
    """
    Follow a series of steps ("left" or "right") in a binary tree.

    Parameters:
        t (BinaryTree): The root of the binary tree.
        s (list): A list of steps, where each step is "left" or "right".

    Returns:
        The value of the node reached after following the steps,
        or None if a step goes out of bounds.
    """
    current = t  # Start traversal at the root of the tree.
    for step in s:  # Iterate over each step in the provided list.
        if current is None:
            # If we reach a None node, stop traversal.
            break  # Exit the loop since we can't proceed further.
        if step == "left":
            # If the step is "left", move to the left child.
            current = current.left_child
        elif step == "right":
            # If the step is "right", move to the right child.
            current = current.right_child
    # Return the value of the node reached, or None if traversal ended prematurely.
    return current.value if current else None

def in_range(t, low, high):
    """
    Check if all values in a binary tree satisfy low <= value <= high.

    Parameters:
        t (BinaryTree): The root of the binary tree.
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        bool: True if all values in the tree are in the range, False otherwise.
    """
    if t is None:
        # If the tree is empty, it is trivially in range.
        return True
    if not (low <= t.value <= high):
        # If the current node's value is out of range, return False.
        return False
    # Recursively check the left and right subtrees.
    return in_range(t.left_child, low, high) and in_range(t.right_child, low, high)

def in_range_v2(t, low, high):
    """
    Check if all values in a binary tree satisfy the range conditions.
    If `low` or `high` is None, that limit is ignored.

    Parameters:
        t (BinaryTree): The root of the binary tree.
        low (int or None): The lower bound of the range, or None to ignore.
        high (int or None): The upper bound of the range, or None to ignore.

    Returns:
        bool: True if all values in the tree are in the range, False otherwise.
    """
    if t is None:
        # If the tree is empty, it is trivially in range.
        return True

        # if current value is outside range, considering for none limits
    if (low is not None and t.value < low) or (high is not None and t.value > high):
            return False

    # Recursively check the left and right subtrees.
    return in_range_v2(t.left_child, low, high) and in_range_v2(t.right_child, low, high)

def ctree(x, n):
    """
    Create a calculation tree for exponentiation using squares and products.

    Parameters:
        x (int): The base value to exponentiate.
        n (int): The power to which `x` should be raised.

    Returns:
        Tree: The root of the calculation tree.
    """
    if n == 1:
        # Base case: if n is 1, return a tree with the single value `x`.
        return Tree(x)
    if n % 2 == 0:
        # If n is even, use the formula (x^(n/2))^2.
        subtree = ctree(x, n // 2)  # Recursively create the tree for x^(n/2).
        root = Tree("^2")  # Create a root node labeled "^2".
        root.children.append(subtree)  # Add the subtree as its only child.
        return root
    else:
        # If n is odd, use the formula x * x^(n-1).
        subtree = ctree(x, n - 1)  # Recursively create the tree for x^(n-1).
        root = Tree("*")  # Create a root node labeled "*".
        root.children.append(Tree(x))  # Add the base `x` as the first child.
        root.children.append(subtree)  # Add the subtree as the second child.
        return root


# Testing BinaryTree class
bt = BinaryTree(10)
bt.left_child = BinaryTree(5)
bt.right_child = BinaryTree(15)
bt.left_child.left_child = BinaryTree(3)
bt.left_child.right_child = BinaryTree(7)

# Testing BinaryTree class
bt = BinaryTree(10)
bt.left_child = BinaryTree(5)
bt.right_child = BinaryTree(15)
bt.left_child.left_child = BinaryTree(3)
bt.left_child.right_child = BinaryTree(7)

print("### Testing follow function ###")
print("Test 1: follow(bt, ['left', 'right']) -> Expected: 7, Got:", follow(bt, ["left", "right"]))
print("Test 2: follow(bt, ['right']) -> Expected: 15, Got:", follow(bt, ["right"]))
print("Test 3: follow(bt, ['left', 'left']) -> Expected: 3, Got:", follow(bt, ["left", "left"]))
print("Test 4: follow(bt, ['left', 'left', 'right']) -> Expected: None, Got:", follow(bt, ["left", "left", "right"]))

print("\n### Testing in_range function ###")
print("Test 5: in_range(bt, 1, 20) -> Expected: True, Got:", in_range(bt, 1, 20))
print("Test 6: in_range(bt, 6, 20) -> Expected: False, Got:", in_range(bt, 6, 20))
print("Test 7: in_range(bt, 3, 10) -> Expected: False, Got:", in_range(bt, 3, 10))

print("\n### Testing in_range_v2 function ###")
print("Test 8: in_range_v2(bt, None, 15) -> Expected: True, Got:", in_range_v2(bt, None, 15))
print("Test 9: in_range_v2(bt, 5, None) -> Expected: False, Got:", in_range_v2(bt, 5, None))
print("Test 10: in_range_v2(bt, 6, None) -> Expected: False, Got:", in_range_v2(bt, 6, None))

print("\n### Testing ctree function ###")
ct = ctree(2, 8)  # Generate a calculation tree for 2^8
print("Test 11: ctree(2, 8) -> Expected: Structured tree for 2^8, Got:")
print(ct)  # Print the calculation tree for verification
