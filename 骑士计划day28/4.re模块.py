import re
# 从一个字符串中获取要匹配的内容
# findall ****
# 列表

# search  *****      验证用户输入内容 ^正则表达式$
# ret = re.search('^\d+','293ahsdjksahf2938u')
# print(ret)


# match     验证用户的输入内容
# ret = re.match('\d+','293ahsdjksahf2938u')
# print(ret)
# print(ret.group())


# 切割split

# s1 = 'alex|egon|boss_jin'
# s1.split('|')

# s = 'alex83egon20boass_jin'
# ret = re.split('\d+',s)
# print(ret)
#
# ret = re.split('(\d+)',s)
# print(ret)
#
# ret = re.split('\d(\d+)',s)
# print(ret)





# 替换sub
# s1 = 'alex|egon|boss_jin'
# s1.replace('|','-')

# s = 'alex83egon20boass_jin'
# ret = re.sub('\d+','|',s)
# print(ret)
#
# ret = re.sub('\d+','|',s,1)
# print(ret)

# ret = re.subn('\d+','|',s)
# print(ret)



# compile ****  编译正则规则的
# ret= re.compile('\d+')
# print(ret)
# com = ret.findall('abc1cde2fgh3skhfk')
# print(com)
# com = ret.finditer('abc1cde2fgh3skhfk')
# for i in com:
#     print(i.group())



# finditer **** 节省空间的方法
# ret = re.finditer('\d+','abc1cde2fgh3skhfk')
# print(ret)
# for i in ret:
#     print(i.group())





# findall search
# compile finditer










# 分组命名，分组约束
# 前端
# <h1>函数</h1>
# <h2>初始函数</h2>
# 实际上对于前端语言老说，都是把不同样式的字体放在不同的标签中


# <(.*?)>.*?<.*?>
# <(?P<tag>.*?)>.*?</(?P=tag)>

pattern = '<(?P<tag>.*?)>.*?</(?P=tag)>'
ret = re.search(pattern,'<h1>函数</h1>')
if ret:
    print(ret.group())
    print(ret.group(1))



# (?:正则表达式) 表示取消优先显示功能
# (?P<组名>正则表达式) 表示给这个组起一个名字
    # (?P=组名) 表示引用之前组的名字，引用部分匹配到的内容必须和之前那个组中的内容一模一样





