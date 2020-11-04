# 1.匹配整数或者小数（包括整数和负数）
# -?\d+(\.\d+)?

# 2.匹配年月日日期 格式2018-12-31
# [1-9]\d{3}-(0?[1-9]|1[1-2])-([12]\d|3[01]|0?[1-9])

# 3.qq号 5-12
# [1-9]\d{4,11}

# 4.11位电话号码
# 1[3-9]\d{9}

# 5.8-10的用户密码
# \w{8,10}

# 6.匹配验证码
# [0-9a-zA-Z]{4}

# 7.匹配邮箱，邮箱规则
# [\w\-.]+@[\da-zA-Z\-]+(\.[\da-zA-Z]+)*\.[a-zA-Z\d]{2,6}

# 8题
import re
# ret = re.findall('<.*?>(.*?)<.*?>','<a>wahaha</a>')
# print(ret)
# ret2 = re.findall('<(.*?)>(.*?)<.*?>','<a>wahaha</a>')
# print(ret2)

# ret2 = re.search('<(.*?)>(.*?)<.*?>','<a>wahaha</a>')
# print(ret2.group(1))
# print(ret2.group(2))


# 9题
# \{[^()]+\}

# 10题
# \d+(\.\d+)?[*/]-?\d+(\.\d+)?


exp = '2*3/4*5'
while 1:

    ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',exp)

    if ret:
        son_exp = ret.group()
        print(son_exp)
        if '*' in son_exp:
            a,b = son_exp.split('*')
            mul = str(float(a)*float(b))
            exp = exp.replace(son_exp,mul)
        elif '/' in son_exp:
            a, b = son_exp.split('/')
            mul = str(float(a) / float(b))
            exp = exp.replace(son_exp, mul)

    else:break
print(exp)
