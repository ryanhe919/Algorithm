**方法1：BFS**
```python
def levelOrder(root):
    result = []
    stack = [[root, 1]]
    while stack:
        # print(stack)
        node  = stack.pop(0)
        if node[0]:
            if len(result) < node[1]:
                result.append([node[0].val])
            else:            
                stack.append([node[0].left, node[1] + 1])
                stack.append([node[0].right, node[1] + 1])
    return result
```