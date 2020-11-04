# dic = {
#     'name':'汪峰',
#     'age':48,
#     'wife':[{'name':'国际章','age':38}],
#     'children':{'girl_first':'小苹果','girl_second':'小怡','girl_three':'顶顶'}
# }

# 1. 获取汪峰的名字。
# print(dic["name"])
# 2.获取这个字典：{'name':'国际章','age':38}。
# print(dic.get("wife")[0])
# 3. 获取汪峰妻子的名字。
# print(dic.get("wife")[0]["name"])
# 4. 获取汪峰的第三个孩子名字。
# print(dic.get("children")["girl_three"])

# dic1 = {
#     'name':["alex",2,3,5],
#     'job':'teacher',
#     'okdbody':{
#         'alex':['python1','python2',100]
#     }
# }
# 1.将name对应的列表追加一个元素'wusir'
# dic1.get("name").append("wusir")
# print(dic1)
# 2.将name对应的列表中的alex首字母大写
# dic1["name"][0] = dic1.get("name")[0].capitalize()
# print(dic1)
# 3.okdboy对应的字典追加一个键值对"老男孩"，"lunxu"
# dic1.get("okdbody").setdefault("老男孩","lunxu")
# print(dic1)
# 4.将okbody对应的字典中的Alex对应的列表中python删除
# pop() 删除的是下标索引值
# dic1.get("okdbody").get("alex").remove("python1")
# print(dic1)
