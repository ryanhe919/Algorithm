**方法1：** python内置replace函数
``` python
def replaceSpace(s):
    return s.replace(" ", "%20")
```

**方法2：** 遍历字符串

``` python
def replaceSpace(s):
    result = ""
    for i in s:
        if i == " ":
            result += "%20"
        else:
            result += i
    return result
```