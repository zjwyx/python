
# re
import re
# findall
# ret = re.findall('\d+','F93AKFA;2183')
# print(ret)
# 参数：正则表达式 带匹配的字符串
# 返回值 是一个列表，所有匹配到的项




# search
ret = re.search('\d+','F93AKFA;2183')
print(ret.group())
# search
# 返回值：返回一个对象
    # 通过group去取值
    # 且只包含第一个匹配到的值


# 需求
# 有一个字符串'2*3/4*5'

ret = re.search('(\d)[*/]([\d])','2*3/4*5')
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(int(ret.group(1)) * int(ret.group(2)))







# findall 有一个特点，会优先显示分组中的内容
# ret = re.findall('www\.(baidu|oldboy)\.com','www.baidu.com')
# print(ret)
# ?: 取消分组优先
# 'www\.(baidu|oldboy)\.com','www.baidu.com'
# 'www\.(baidu)\.com','www.baidu.com'ret = re.search('www\.(baidu|oldboy)\.com','www.baidu.com')
# baidu


# ret = re.search('www\.(baidu|oldboy)\.com','www.baidu.com')
# print(ret.group())
# print(ret.group(1))
