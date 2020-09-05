def replaceSpace(s):
    return s.replace(" ", "%20")


def replaceSpace_v2(s):
    result = ""
    for i in s:
        if i == " ":
            result += "%20"
        else:
            result += i
    return result