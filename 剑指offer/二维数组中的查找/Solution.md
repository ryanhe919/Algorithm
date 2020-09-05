**方法1：** 带条件遍历

由于数组每一行从小到大排列， 所以判断是否游客可能在某一行及target 大于一行的第一个元素小于最后一个元素。如果条件满足，再遍历该行。
``` python
def findNumberIn2DArray(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    for row in matrix:
        if row[0] <= target and row[-1] >= target:
            for num in row:
                if num == target:
                    return True
    return False
```