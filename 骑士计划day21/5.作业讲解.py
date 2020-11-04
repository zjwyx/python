# 场景，角色，类 - 属性和方法
# 站在每个角色的角度上去思考程序执行的流程
import sys
class Course:
    def __init__(self,name,price,period,teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

class Student:
    openate_lst = [('查看可选课程', 'show_course'),
                   ('选择课程', 'select_course'),
                   ('查看已选课程', 'check_selected_course'),
                   ('退出', 'exit')]
    def __init__(self,name):
        self.name = name
        self.courses = []

    def show_course(self):
        print('查看可选课程')

    def select_course(self):
        print('选择课程')

    def check_selected_course(self):
        print('查看已选课程')

    def exit(self):
        exit()

class Manager:
    openate_lst = [('创建课程','create_course'),
                   ('创建学生','create_student'),
                   ('查看所有课程','show_course'),
                   ('查看所有学生','show_student'),
                   ('查看所有学生的选课情况','show_student_course'),
                   ('退出','exit')]
    def __init__(self,name):
        self.name = name

    def create_course(self):
        print('创建课程')

    def create_student(self):
        print('创建学生')

    def show_course(self):
        print('查看所有的课程')

    def show_student(self):
        print('查看所有学生')

    def show_student_course(self):
        print('查看所有学生的选课情况')

    def exit(self):
        exit()


# 学生：登录就可以选课了
    # 有学生
    # 有课程了

# 管理员：
    # 学生的账号是管理员创建的
    # 课程也应该是管理员创建的

# 应该先站在管理员的角度来开发
# 登录
# 登录必须能够自动识别生份
# 用户名/密码/自动识别生份

def login():
    name = input('username:')
    pawd = input('password:')
    with open('userinfo',encoding='utf-8') as f:
        for line in f:
            usr,pwd,identify = line.strip().split('|')
            if usr == name and pwd == pawd:
                return {'result':True,'name':name,'id':identify}
            else:
                return {'result':False,'name':name}

ret = login()

if ret['result']:
    print('登录成功')
    if hasattr(sys.modules[__name__],ret['id']):
        cls = getattr(sys.modules[__name__],ret['id'])
        obj = Manager(ret['name'])
        for id,item in enumerate(Manager.openate_lst,1):
            print(id,item[0])
        func_str = Manager.openate_lst[int(input('>>>')) - 1]
        if hasattr(obj,func_str):
            getattr(obj,func_str)()

    # if ret['id'] == 'Manager':
    #     obj = Manager(ret['name'])
    #     for id,item in enumerate(Manager.openate_lst,1):
    #         print(id,item[0])
    #     func_str = Manager.openate_lst[int(input('>>>')) - 1]
    #     if hasattr(obj,func_str):
    #         getattr(obj,func_str)()
    # elif ret['id'] == 'Student':
    #     obj = Manager(ret['name'])
    #     for id, item in enumerate(Manager.openate_lst, 1):
    #         print(id, item[0])
    #     func_str = Manager.openate_lst[int(input('>>>')) - 1]
    #     if hasattr(obj, func_str):
    #         getattr(obj, func_str)()
