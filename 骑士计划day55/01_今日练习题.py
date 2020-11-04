'''
python全栈课前练习题
'''

# s = 'Alex SB 哈哈\r\nx:1\r\ny:2\r\nz:3\r\n\r\n自行车'
#
# # 问题1：如何取到['Alex SB 哈哈\r\nx:1\r\ny:2\r\nz:3','自行车']
# list1 = s.split('\r\n\r\n')
# print(list1)
#
# # ['Alex SB 哈哈\r\nx:1\r\ny:2\r\nz:3', '自行车']
# # 问题2：如何在上面结果基础上拿到['alex','SB','哈哈']
# list2 = list1[0].split('\r\n')
# list3 = list2[0].split(' ')
# print(list3)
#
# # 问题3：如何在上面结果基础向拿到SB?
# list4 = list3[1]
# print(list4)




# 有一个列表，他的内部是一些元组，元组的第一个元素是姓名，第二个是爱好
# 现在我给你一个姓名，如‘Egon’，如果有这个姓名，就打印出它的爱好，没有就打印查无此人

# list1 = [
#     ('alex','烫头'),
#     ('Egon','街舞'),
#     ('Yuan','喝茶')
# ]
# for i in list1:
#     if i[0] == 'Egon':
#         print(i[1])
#         break
# else:
#     print('查无此人')




# 我们有一个HTML文件login.html
# 问题1：我如何读取它的内容保存到变量html_s
# with open('login.html',mode='r',encoding='utf8') as f1:
#     html_s = f1.read()
# print(html_s)
# # 问题2：我如何读取它的二进制内容保存到变量html_b
# with open('login.html',mode='rb') as f2:
#     html_b = f2.read()
# print(f2)

s2 = 'Alex 花了一百万买了辆电动车 ，真@@xx@@'
# 问题1：如何把s2转变成'Alex 花了一百万买了辆电动车 ，真sb'
print(s2.replace('@@xx@@','SB'))