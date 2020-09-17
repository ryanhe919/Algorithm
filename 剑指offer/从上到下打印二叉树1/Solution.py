def levelOrder(root):
    stack = [root]
    result = []
    while stack:
        node = stack.pop(0)
        if node:
            result.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return result