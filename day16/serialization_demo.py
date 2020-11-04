'''
序列化
'''

# 序列化：将内存中的数据转化策划稿字符串，用以保存在文件或通过网络传输，成为路劣化过程
# 反序列化：从文件中。网络中获取的数据，转化成内存中原来的数据类型成为反序列化过程


# json 模块：将数据转化成字符串，用于存储或网络传输
import json

# 把指定的对象转化成json格式的字符串
# res = json.dumps([1,2,3])
# print(res)   # '[1,2,3]'
# print(type(res))

# 元组可以序列化，最后成为列表
# s = json.dumps((1,2,3))
# print(s)
# print(type(s))

# 整型变json
# s = json.dumps(10)
# print(s)
# print(type(s))

# 字典变json
# s = json.dumps({'name':'alex','age':10})
# print(s)
# print(type(s))


# 将json结果写到文件中
# with open('a.txt',mode='at',encoding='utf-8') as f:
#     json.dump([1,2,3],f)



# 反系列化（字符串变列表）
# res = json.dumps([1,2,3])
# let = json.loads(res)
# print(let)
# print(type(let))

# 元组会变成列表
# res = json.dumps((1,2,3))
# let = json.loads(res)
# print(let)
# print(type(let))

# 从文件中反序列化
# with open('a.txt',encoding='utf-8') as f1:
#     ret = json.load(f1)
#     print(ret)
#     print(type(ret))



# 总结：
# json.dumps(obj)
# json.dump(obj,f)
# json.loads(s)
# json.load(j)


# json文件通常是一次性读，一次性写
# 使用另外一种方式可以实现多次写，多次度

# 把需要序列化的对象，通过多次序列化的方式，用文件的wirte方法，把多次序列化的即送字符串
with open('json.txt',encoding='utf-8',mode='wt') as f1:
    f1.write(json.dumps([1,2,3]) + '\n')
    f1.write(json.dumps([1,5,6]) + '\n')


# 把分次序列化的json字符串，反序列化回来
with open('json.txt',encoding='utf-8') as f1:
    for i in f1:
        print(json.loads(i.strip()))

