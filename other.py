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
