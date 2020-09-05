def findNumberIn2DArray(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    for row in matrix:
        if row[0] <= target and row[-1] >= target:
            for num in row:
                if num == target:
                    return True
    return False