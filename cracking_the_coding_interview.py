#4.2 Minimal tree
import math
from typing import List

from loguru import logger

input = []

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"data={self.data},left=[{self.left if self.left else ''}],right=[{self.right if self.right else ''}]"

def minimal_tree(int_list: List) -> TreeNode:
    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return TreeNode(int_list[0], None, None)
    middle_index = len(int_list)//2
    return TreeNode(int_list[middle_index], minimal_tree(int_list[:middle_index]), minimal_tree(int_list[middle_index+1:]))

#4.3 list of depths
def list_depths(root: TreeNode, lists: List = {}, level = 0) -> List:
    if root is None: return []

    if (len(lists) == level):
        level_list = []
    else:
        level_list = lists[level]

    level_list.append(root.data)
    lists[level] = level_list

    list_depths(root.left, lists, level+1)
    list_depths(root.right, lists, level+1)
    return lists

#4.4 check if balanced
def check_height(root):
    if root is None: return -1

    left_height = check_height(root.left)
    if left_height == -math.inf: return -math.inf

    right_height = check_height(root.right)
    if right_height == -math.inf: return -math.inf

    height_diff = left_height-right_height
    if (abs(height_diff) > 1 ):
        return -math.inf
    else:
        return max(left_height,right_height) + 1


def is_balanced(root: TreeNode) -> bool:
    return check_height(root) != -math.inf


#4.5 Validate BST - using min/max
def is_bst(node,min=-math.inf, max=math.inf) -> bool:
    if node is None:
        return True
    if float(node.data) > max or float(node.data) <= min:
        return False
    if not is_bst(node.left,min, node.data) or not is_bst(node.right, node.data, max):
        return False
    return True

#10.2 group anagrams


if __name__ == '__main__':
    child_node = TreeNode(5,TreeNode(1, None, TreeNode(1, None, None)), TreeNode(1, TreeNode(1, None, None), None))
    small_child_node = TreeNode(1,None, None)

    second_child_node = TreeNode(10,TreeNode(8, None, TreeNode(9, None, None)), TreeNode(12, TreeNode(11, None, None), None))
    tree = TreeNode(4, child_node,second_child_node)
    bst = TreeNode(4,small_child_node, second_child_node)
    # result = is_balanced(tree)
    result = is_bst(bst)

    print(result)