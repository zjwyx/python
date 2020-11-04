# 文件操作
class File:
    lst = [('读文件','read'), ('写文件','write'), ('删除文件','remove'), ('文件的重命名','rename'), ('复制','cpoy')]
    def __init__(self,filepath):
        self.filepath = filepath

    def write(self):
        print('in write func')
    def read(self):
        print('in read func')
    def remove(self):
        print('in remove func')
    def rename(self):
        print('in rename func')
    def copy(self):
        print('in copy func')



f = File('dsafdsa')
while 1:
    for index,opt in enumerate(File.lst,1):
        print(index,opt[0])

    num = int(input('请输入你要做的操作序号>>>'))

    # print(File.lst[num-1][1])
    if hasattr(f,File.lst[num-1][1]):
        getattr(f,File.lst[num-1][1])()

# if num == '1':
#     f.read()
# elif num == '2':
#     f.write()
# elif num == '3':
#     f.remove()
# elif num == '4':
#     f.rename()
# elif num == '5':
#     f.copy()


# 显示所有可以做的操作
# 1.读文件
# 2.写文件
# 3.删除文件
# 4.文件的重名民

