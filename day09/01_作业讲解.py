#通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。

l1 = []
l2 = ['name','price','amount']
with open('a.txt',encoding='utf-8') as f1:
    for old in f1:
        line_list = old.strip().split()
        dic = {}
        for i in range(len(l2)):
            dic[l2[i]] = line_list[i]
        l1.append(dic)
print(l1)
