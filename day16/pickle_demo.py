'''
pickle:
将python中所有的数据类型转化成字节串，序列化过程
将字节串转化成python中数据类型，反序列化过程
'''


import pickle

# bys = pickle.dumps([1,2,3])
# # <class 'bytes'>
# print(type(bys))
# # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
# print(bys)


# 保存了元组的数据类型
# bys = pickle.dumps((1,2,3))
#
# res = pickle.loads(bys)
# print(type(res))


# 所欲的数据类型都可以进行序列化
# bys = pickle.dumps(set({'1','2'}))
#
# res = pickle.loads(bys)
# print(type(res))


# 把pickle序列化的内容写入文件中
# with open('c.txt',mode='wb') as f1:
#     pickle.dump([1,2,3],f1)


# 从文件中反序列化prickle数据
# with open('c.txt',mode='rb') as f2:
#     res = print(pickle.load(f2))
#     print(type(res))
#     print(res)



# 多次把pickle序列化的内容写入文件中
# with open('c.txt',mode='ab') as f1:
#     pickle.dump([1,2,3],f1)
#     pickle.dump([1,2,3],f1)
#     pickle.dump([1,2,3],f1)


# with open('c.txt',mode='rb') as f2:
#     for i in range(4):
#         res = pickle.load(f2)
#         print(res)


# pickle常用的场景和json一样，一次性写入，依次是读取


# json和pickle的比较
'''
json:
1.不是所有的数据类型都可以序列化，结果是字符串
2.不能多次对同一个文件序列化
3.json数据可以跨语言

pickle：
1.所有python类型都可以序列化，结果是字节串
2.可以多次对同一个文件序列化
3.不能跨语言



文件操作
rt：文本形式读取(t:text)
rb：bytes类型读(b:bytes)(rb,wb,ab)
'''




























