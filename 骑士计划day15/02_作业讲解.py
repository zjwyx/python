
# 用map来处理字符串列表，把列表中所有人都变为sb，比方alex_sb
# name = ['oldboy','alex','wusir']
# ret = map(lambda a: a + '_sb',name)
# print(list(ret))


# 用map来处理下述，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l = [{'name':'alex'},{'name':'y'}]
# print(list(map(lambda a:a['name'] + 'sb',l)))
# print([i['name'] + 'sb' for i in l])

# 6 用filter来处理，得到股票价格大于20的股票名字
shares = {
    'IBM':36.6,
    'Lenovo':23.2,
    'oldboy':21.2,
    'ocean':10.2
}
def func(a):
    return shares[a] > 20
print(list(filter(func,shares)))


# 详见第十四天作业讲解
