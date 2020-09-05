**方法1：** 递归

``` python
def buildTree(preorder, inorder):
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    left_length = inorder.index(preorder[0]) + 1
    root.left = buildTree(preorder[1:left_length], inorder[0:left_length - 1])
    root.right = buildTree(preorder[left_length:], inorder[left_length:])
    return root
```