**快速排序**

**原理：** 递归的方式每次选择数组中的一个数字, 把小于该数字的放在左边, 大于的放在右边, 直到数组只有一个或空.

``` python
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

```
 