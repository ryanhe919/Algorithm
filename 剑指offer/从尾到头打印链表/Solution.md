**方法1：** 遍历

先顺序遍历保存数值到List， 再翻转List。
``` python
def reversePrint(head):
    result = []
    while head != None:
        result.append(head.val)
        head = head.next
    result.reverse()
    return result
```