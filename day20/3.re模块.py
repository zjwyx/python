import re


# 先compile（如果没有重复使用同一个正则，也不能节省时间）
# 再finditer，既节省时间又节省空间
com = re.compile('\d+')
ret = com.finditer('agksak018as093')

for i in ret:
    print(i.group())
