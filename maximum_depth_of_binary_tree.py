from common.treenode import TreeNode


def maxDepth(root: TreeNode) -> int:
    """
    time: n
    space: n        (log n for perfectly balanced tree)
    """
    # if not root:
    #     return 0
    # return 1 + max(maxDepth(root.left), maxDepth(root.right))

    """
    time: n
    space: n
    """
    stack = []
    if root:
        stack.append((1, root))

    max_depth = 0
    while stack != []:
        cur_depth, root = stack.pop()
        if root:
            max_depth = max(cur_depth, max_depth)
            stack.append((1 + cur_depth, root.left))
            stack.append((1 + cur_depth, root.right))

    return max_depth