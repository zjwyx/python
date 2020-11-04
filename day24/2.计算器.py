from functools import reduce

# exp = (1+3*4*5/6)-4
# 计算两个数的乘法或者除法
def mul_div(exp):
    if '*' in exp:
        a,b = exp.split('*')
        return float(a) * float(b)
    if '/' in exp:
        a,b = exp.split('/')
        return float(a) / float(b)
    if '+' in exp:
        a,b = exp.split('+')
        return float(a) + float(b)
    if '-' in exp:
        a,b = exp.split('-')
        return float(a) - float(b)



# # 计算表达式中的所有乘除法
# # 1+3*4*5/6
#
# ret = mul_div('3.12*4.56')
# print(ret)


import re

def emp_fmt(exp):
    while re.search('[+-]{2,}',exp):
        exp = exp.replace('--','+')
        exp = exp.replace('+-','-')
        exp = exp.replace('-+','-')
        exp = exp.replace('++','+')
    return exp

def remove_addsub(exp):

    ret = re.findall('[-+]?\d+(?:\.\d+)?',exp)
    print(ret)
    res = reduce(lambda a,b : float(a) + float(b),ret)
    return res
    # count = 0
    # for i in ret:
    #     count += float(i)
    # print(count)

# 计算加减法
# exp = '1+2.23-++317+-429-5+6'
# exp = emp_fmt(exp)
# ret = remove_addsub(exp)
# print(ret)


def remove_muldiv(exp):
    while 1:
        ret = re.search('\d+(\.\d+)?[*/]-?\d(\.\d+)?',exp)
        if ret:
            son_exp = ret.group()
            res = mul_div(son_exp)
            print(res)          # 12
            exp = exp.replace(son_exp,str(res))
            print(exp)          # 1+12.0*5/6
        else:
            break
    return exp

# 计算乘除法
# ret = remove_muldiv('1+3*4*5/6')
# print(ret)

