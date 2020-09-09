**方法1：DFS**
``` python
def combinationSum(candidates, target):
    result = []
    stack = []
    for i in candidates:
        if i <= target:
            stack.append([i])
    while stack:
        path = stack.pop()
        if sum(path) == target and sorted(path) not in result:
            result.append(sorted(path))
        else:
            for i in candidates:
                new_path = path[:]
                if i + sum(new_path) <= target:
                    new_path.append(i)
                    stack.append(new_path)
    return sorted(result)
```