from common.treenode import TreeNode


def searchBST(root: TreeNode, val: int) -> TreeNode:
    # """
    # time: h
    # space: h
    # """
    # if not root or root.val == val:
    #     return root
    #
    # return searchBST(root.left, val) if val < root.val else searchBST(root.right, val)

    """
    time: h
    space: 1
    """
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root

