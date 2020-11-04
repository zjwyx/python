# 制作一个公共的模板
# 让一个字符串的某些之变成动态的值
# name = input("请输入你的姓名:");
# age = input("请输入你的年龄:");
# job = input("请输入你的工作:");
# hobby = input("请输入你的爱好:");
# #  %-占位符   s--"str"
# mag = '''- - - - - - - - -  info of %s   - - - - - -
#  Name : %s
#  Age : %s
#  job : %s
#  Hobbie : %s
#  - - - - - - - - -  end  - - - - - - - - - ''' % (name,name,age,job,hobby)
# print(mag);


# 坑，在格式输出中，%只想表示一个百分号，而不是作为占位符使用



name = input("请输入姓名:");
age = input("请输入年龄:");
sex = input("请输入性别:");

mag = "你的名字%s, 你的年龄%s,你的性别为%s" % (name,age,sex);
print(mag)










