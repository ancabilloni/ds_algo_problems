# Src: Hackerrank. Category: Trees. Difficulty: Medium
# Question: check if the tree is BST which satisfy conditions:
# - All data on the left subtree must be less than the current node's data
# - All data on the right substree must be greater than the current node's data
# - All nodes' data are unique in the tree

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
"""
Less efficient method:
- If node is Null, return True
- At every node, check for maxLeft >= node.data or maxRight <= node.data, then return False
- Recurse to check the left and right node
- Write helper functions minNode and maxNode

Time complexity: O(nlogn)
"""
# def minNode(root):
#     _min = root.data
#     node = root
#     while node.left:
#         if _min > node.left.data:
#             _min = node.left.data
#         node = node.left
#     return _min

# def maxNode(root):
#     _max = root.data
#     node = root
#     while node.right:
#         if _max < node.right.data:
#             _max = node.right.data
#         node = node.right
#     return _max


# def checkBST(root):
#     if root is None:
#         return True
    
#     if root.right and minNode(root.right) <= root.data:
#         return False
    
#     if root.left and maxNode(root.left) >= root.data:
#         return False
    
#     if not checkBST(root.left) or not checkBST(root.right):
#         return False
#     return True


'''
Efficient way: 
- Visit every node once, check the condition:
 + If node is Null -> it is BST
 + If node min_limit >= node -> it is not BST
 + If node max_limit <= node -> it is not BST
 + Return recursive result of both left and right children:
    - For Left child, min_limit = parent's min, max_limit = parent
    - For Right child, min_limit = parent, max_limit = parent's max
Time complexity: O(n). Space O(1)
'''
def checkBST(root, l=None, r=None):
    if root is None:
        return True
    
    if l and l.data >= root.data:
        return False
    
    if r and r.data <= root.data:
        return False
    
    return checkBST(root.left, l, root) & checkBST(root.right, root, r)
