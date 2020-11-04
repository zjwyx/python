# li = [i for i in range(100)]
# # li === bytes
# # bl = li.encode='utf-8' 不能直接转化
# # li转化成字符串在转化成bytes
# s1 = str(li)
# b1 = s1.encode('utf-8')
# print(b1)




# str我们学过的str

# dic = {'name':'太白','password':123,'status':True}
import json
# dumps loads 主要用于网络传输，但是也可以读写文件
# 特殊的字符串
# st = json.dumps(dic,ensure_ascii=False)
# print(type(st))
# print(st)
# # 反转回去
# dic1 = json.loads(st)
# print(dic1,type(dic1))



# 写文件
# l1 = [1,2,3,{'name':'alex'}]
# 转化成特殊的字符串写入文件
# with open('json文件',encoding='utf-8',mode='w') as f1:
#     st = json.dumps(l1)
#     f1.write(st)


# 读取出来还原回去
# with open('json文件',encoding='utf-8') as f2:
#     st = f2.read()
#     l1 = json.loads(st)
#     print(l1)
#     print(type(l1))

l1 = [1,2,3,{'name':'alex'}]
# dump load 只能写入文件，只能写入一个数据结构
# with open('json文件1',encoding='utf-8',mode='w') as f1:
#     json.dump(l1,f1)


# with open('json文件1',encoding='utf-8') as f2:
#     f1 = json.load(f2)
#     print(f1,type(f1))


# 一次写入多个数据怎么做？
# 错误数据
# dic1 = {'username':'alex'}
# dic2 = {'username':'太白'}
# dic3 = {'username':'大壮'}
# with open('json文件1',encoding='utf-8',mode='w') as f1:
#     json.dump(dic1,f1)
#     json.dump(dic2,f1)
#     json.dump(dic3,f1)

# 读取数据
# with open('json文件1',encoding='utf-8') as f2:
#     f1 = json.load(f2)
#     print(f1,type(f1))



# 正确写法：
# dic1 = {'username':'alex'}
# dic2 = {'username':'太白'}
# dic3 = {'username':'大壮'}
# with open('json文件1',encoding='utf-8',mode='w') as f1:
#     f1.write(json.dumps(dic1) + '\n')
#     f1.write(json.dumps(dic2) + '\n')
#     f1.write(json.dumps(dic3) + '\n')

# with open('json文件1',encoding='utf-8') as f2:
#     for i in f2:
#         print(json.loads(i))

