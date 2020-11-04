# id，name，age，phone，job
# 1，alex，22,13651504608，IT
# 2，egon，23,13304320533，Teacher
# 3，nezha，25,13332355322，IT



# 对于文件的
# 增，删，改，查
# 增

def add(sql):
    # 字符串方法：replace 替换
    sql = sql.replace(' ','')
    with open('record',encoding='utf-8') as f2:
        index = int(f2.read())
    line = f'{index + 1},{sql}\n'
    with open('record', encoding='utf-8',mode='w') as f2:
        f2.write(str(index + 1))
    with open('staff_info',encoding='utf-8',mode='a') as f1:
        f1.write(line)


def read_line():
    with open('staff_info', encoding='utf-8') as f:
        for i in f:
            lst = i.strip.split(',')
            yield lst



def select(sql):
    dic = {'id': 0,'name':1,'age':2,'phone':3,'job':4}
    # print(sql)
    sql = sql.replace(' ','')
    # print(sql)
    col,con = sql.split('where')
    print(col,con)
    # 先根据条件进行筛选
    if '>' in con:
        con_name,val = con.split('>')

        for lst in read_line():
            if int(lst[dic[con_name]]) > int(val):
                # 根据要求显示的列进行显示
                col_lst = col.split(',')
                for c in col_lst:
                    print(lst[dic[c]],end=' ')
                print('\n')

    if '<' in con:
        con_name, val = con.split('<')
        for lst in read_line():
            if int(lst[dic[con_name]]) < int(val):
                # 根据要求显示的列进行显示
                col_lst = col.split(',')
                for c in col_lst:
                    print(lst[dic[c]], end=' ')
                print('\n')
    'age>22'
    'age<22'
    'age=22'
    # 根据哟啊显示的列进行显示

# 字符串方法：startswith 判断是否以add开头
while 1:

    sql = input('>>>:')  # add alex，22,13651504608，IT
    if sql == 'q':
        break
    elif sql.startswith('add'):
        lst = sql.split('add')
        add(lst[1])
    elif sql.startswith('select'):
        lst = sql.split('select')
        select(lst[1])

# add alex，22,13651504608，IT
    # alex，22,13651504608，IT 按照逗号分隔开
# 第一个值必须是字母开头的，第二个值必须是全数字，第三个值必须是11位全数字，最后一个20个字符


# 基本
    # 功能
    # 安全
# 进阶
    # 性能
        # 空间
        # 时间
    # 简洁度：用很少的代码实现更多的功能
    # 可读性：让其他人能更容易的读懂代码
