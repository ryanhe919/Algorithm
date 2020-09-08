def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = unsorted_list[0]
    left = []
    right = []
    for i in range(1, len(unsorted_list)):
        if unsorted_list[i] <= mid:
            left.append(unsorted_list[i])
        if unsorted_list[i] > mid:
            right.append(unsorted_list[i])
    return quicksort(left) + [mid] + quicksort(right)


def mergesort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    return merge(mergesort(unsorted_list[:mid]), mergesort(unsorted_list[mid:]))
    
def merge(left, right):
    l, r = 0, 0
    merged_list = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged_list.append(left[l])
            l += 1
        else:
            merged_list.append(right[r])
            r += 1
    merged_list += left[l:]
    merged_list += right[r:]
    return merged_list