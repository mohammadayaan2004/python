"""a="     i am ayaan khan    "
print(a)
print(a.strip())"""

# strip function remove spaces from the string
def removeAndStrip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()


a="     i am mohammad ayaan khan    "
n= removeAndStrip(a,"ayaan")
print(n)   