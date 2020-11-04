
# %s format
# name = 'alex'
# age = 18
# msg = '我叫%s,今年%s岁了' %(name,age)
# msg1 = '我叫{},今年{}岁了'.format(name,age)
# print(msg)
# print(msg1)


# 新特性，格式化输出
# name = 'alex'
# age = 18
# msg = f'我叫{name},今年{age}岁了'
# print(msg)

# 可以加表达式
# dic = {'name':'alex','age':12}
# msg = f'我叫{dic["name"]},今年{dic["age"]}岁了'
# print(msg)

#
# count = 7
# print(f'最终结果：{count**2}')
# name = 'barry'
# mag = f'我的名字是{name.upper()}'
# print(mag)

# 结合函数写
def sum(a,b):
    return a + b

msg = f'最终结果为：{sum(10,20)}'
print(msg)

# 优点：
# 1.结构更简化
# 2.可以结合表达式，函数进行使用
# 3.效率提升很多