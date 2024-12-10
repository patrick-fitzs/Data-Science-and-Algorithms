class BinaryTree:
    # Represents a binary tree node with a value and optional left and right children.
    def __init__(new_tree, v):
        new_tree.value = v  # Initialize the value of the node.
        new_tree.left_child = None  # Initialize the left child as None.
        new_tree.right_child = None  # Initialize the right child as None.

    # String representation for easy debugging and visualization of the tree.
    def __str__(root):
        s = str(root.value)  # Start with the root value.
        s += " <"  # Begin child representation.
        child_strings = []
        left = root.left_child
        right = root.right_child
        if left != None or right != None:
            child_strings.append(str(left))  # Add the left child representation.
            child_strings.append(str(right))  # Add the right child representation.
        s += ", ".join(child_strings)  # Join child strings with a comma.
        s += ">"  # End child representation.
        return s

    def __repr__(root):
        return str(root)  # Use the string representation for the repr method.


class Tree:
    # Represents a general tree node with a value and a list of children.
    def __init__(new_tree, v):
        new_tree.value = v  # Initialize the value of the node.
        new_tree.children = []  # Initialize an empty list for children.

    # String representation for easy debugging and visualization of the tree.
    def __str__(root):
        s = str(root.value)  # Start with the root value.
        s += " <"  # Begin child representation.
        child_strings = []
        for child in root.children:
            child_strings.append(str(child))  # Add each child's string representation.
        s += ", ".join(child_strings)  # Join child strings with a comma.
        s += ">"  # End child representation.
        return s

    def __repr__(root):
        return str(root)  # Use the string representation for the repr method.

def follow(t, s):
    # Navigates the binary tree based on a sequence of "left" or "right" steps.
    current = t  # Start at the root node.
    for step in s:  # Iterate over the steps in the sequence.
        if current is None:  # Stop if the current node is None.
            break
        if step == "left":  # Move to the left child if the step is "left".
            current = current.left_child
        elif step == "right":  # Move to the right child if the step is "right".
            current = current.right_child
    return current.value if current else None  # Return the value of the final node or None.

def nearest(t):
    # Finds the shortest path to a node with value 5 using BFS.
    from collections import deque

    queue = deque([(t, 0)])  # Initialize the queue with the root and depth 0.

    while queue:  # Continue while there are nodes to process.
        node, depth = queue.popleft()  # Get the next node and its depth.

        if node.value == 5:  # Check if the current node's value is 5.
            return depth  # Return the depth if the value is found.

        if node.left_child:  # Add the left child to the queue if it exists.
            queue.append((node.left_child, depth + 1))

        if node.right_child:  # Add the right child to the queue if it exists.
            queue.append((node.right_child, depth + 1))

    return -1  # Return -1 if no node with value 5 is found.

def in_range(t, low, high):
    # Checks if all nodes in the binary tree are within the range [low, high].
    if t is None:  # If the node is None, it's not in the range.
        return False

    if not (low <= t.value <= high):  # Check if the node's value is within the range.
        return False

    left_in_range = in_range(t.left_child, low, high)  # Check the left subtree.
    right_in_range = in_range(t.right_child, low, high)  # Check the right subtree.

    return left_in_range and right_in_range  # Return True if both subtrees are in range.

def in_range_v2(t, low, high):
    # Checks if all nodes in the binary tree satisfy the range with optional limits.
    if t is None:  # If the node is None, it's not in the range.
        return False

    if low is not None and t.value < low:  # Check the lower limit if provided.
        return False

    if high is not None and t.value > high:  # Check the upper limit if provided.
        return False

    left_in_range = in_range_v2(t.left_child, low, high)  # Check the left subtree.
    right_in_range = in_range_v2(t.right_child, low, high)  # Check the right subtree.

    return left_in_range and right_in_range  # Return True if both subtrees are in range.

def ctree(x, n):
    # Creates a calculation tree for x^n using squares ("^2") and products ("*").
    if n == 0:  # Base case: x^0 = 1.
        return Tree(1)

    if n == 1:  # Base case: x^1 = x.
        return Tree(x)

    if n % 2 == 0:  # If n is even, use the square of x^(n//2).
        subtree = ctree(x, n // 2)  # Create the subtree for x^(n//2).
        root = Tree("^2")  # Create a root node representing squaring.
        root.children.append(subtree)  # Add the subtree as a child.
        return root

    else:  # If n is odd, use x^(n-1) * x.
        subtree = ctree(x, n - 1)  # Create the subtree for x^(n-1).
        root = Tree("*")  # Create a root node representing multiplication.
        root.children.append(subtree)  # Add the subtree as the first child.
        root.children.append(Tree(x))  # Add x as the second child.
        return root
