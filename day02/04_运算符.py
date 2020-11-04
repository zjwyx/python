# and or not
# 1.在没有（）的情况下，优先级：not > and > or,同一优先级从左只有一次计算
# 情况1:两边都有比较运算符
# 情况2：两边都是整数
'''
x or y ,x为真，值就是x，x为假，值是y
'''

# str --- int ：只能是纯数字组成的字符串
# str = "100";
# print(int(str),type(int(str)))
# int ---- str
# a = 100
# print(str(a),type(str(a)))

# int --- bool   非零即true ，0为false
# a = 0;
# print(bool(a))
# bool--- int
# a = True;
# print(int(a))
# a = False;
# print(int(a))


# 思考题
# 比较运算符  >  逻辑运算符
print(1 > 2 and 3 or 6)


# and  or  not
# 优先级：() > not > and > or
# 第二种情况：前后两端的条件为数值
'''
x or y if x is true , return x
'''

# 补充
# int 《======》bool
# 0 对应的bool值为false，非0都是true
# true      1  false   0
# print(bool(0))
# print(int(True))
# print(int(False))
# print(1 or 2)
# print(0 or 6)

# print(1 > 2 or 3 and 4 < 6)

# 应用：
# 1，if while 等条件判断
# 2.面试
