**方法1：**哈希表

``` python
def findRepeatNumber(nums):
    hash_set = set()
    for i in nums:
        if i not in hash_set:
            hash_set.add(i)
        else:
            result = i
            break
    return result
```