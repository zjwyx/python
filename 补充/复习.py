# 基础数据类型的复习
# 整型，布尔值，字符串，字典，元组，集合
# 1.字符串         不可变数据类型
    # 方法
        # 首字母大写，全部大写，全部小写
        # start以什么开头，end以什么结尾
        # find，index 按照元素查找索引
        # 公共方法：count，len
        # replace替换 center 居中
    # 索引和切片

# 2.列表 list     可变的数据类型
    # 索引和切片
        # lit = [1,2,3]
        # 索引lit[0],切片lit[::2]
    # 方法
        # 增
            # append()
            # insert() 需要两个参数 在哪个位置插入什么值
            # extend() 可迭代对象

        # 删
            # remove()
            # pop()  有返回值
            # del

        # 改
            # lit[1] = 'alex'

        # 查
            # for 循环
# 3.元组
    # 只能查看，不能增删改

# 4.字典   {}
# dic = {
#     "name":"太白",
#     "age":18,
#     "hobby_list":['直男',"开车"]
# }
    # 字典的方法
        # 增     有则改之无则加勉
            # dic['sex'] = '男'
            # print(dic)

            # dic.setdefault('sex','男')
            # print(dic)

            # update(sex='男')

        # 删
            # pop()
            # clear()
            # del

        # 改
            # dic['name'] = 'alex'

            # update()
        # 查
            # let = dic.get('name')
            # print(let)
        # 三个特殊的方法
            # keys()
            # values()
            # items()
# 5.集合  set {}
    # 增
        # add()
        # update()  里面的参数是字典，有则改之无则增加

    # 删
        # remove() 按照元素删除
        # pop() 随机删除

# is id == 的区别