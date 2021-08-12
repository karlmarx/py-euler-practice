##check if valid binary tree

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    @staticmethod
    def is_bst(node: TreeNode, last_printed = None) -> bool:
        if node is None:
            return True

        if not Tree.is_bst(node.left, last_printed): return False

        if last_printed and node.data <= last_printed:
            return False

        last_printed = node.data

        if not Tree.is_bst(node.right, last_printed): return False

        return True

if __name__ == "__main__":
    child_node = TreeNode(1,None, None)
    second_child_node = TreeNode(3,None, None)
    test_tree = Tree(root)

    print(Tree.is_bst(second_child_node))






##merge sort


def merge(left,right) -> list:
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def merge_sort(unsorted: list) -> list:
    list_lenth = len(unsorted)
    if list_lenth== 1:
        return unsorted
    mid_point = list_lenth//2
    # left = unsorted[:mid_point]
    # right = unsorted[mid_point:]

    left = merge_sort(unsorted[:mid_point])
    right = merge_sort(unsorted[mid_point:])

    print(f"l{left}r{right}")

    merged = merge(left,right)
    print(merged)
    return merged


def fibonacci_dynamic_programming_memo(n: int, cache=None) -> int:
    if n==1 or n==0:
        return 1
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    else:
        result = fibonacci_dynamic_programming_memo(n-1, cache) + fibonacci_dynamic_programming_memo(n-2, cache)
        cache[n] = result
        return result

