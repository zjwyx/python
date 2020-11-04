# def func():
#     count = 1
#     while 1:
#         count += 1
#         print(count)
#         return
# func()
#
# def func(x,y):
#     return x + y
# func(1,3)

import os

def func(path,old,new):
    with open(path,encoding='utf-8') as f1,\
        open(path + '.bat',encoding='utf-8',mode='w') as f2:
        for old_low in f1:
            new_low = old_low.replace(old,new)
            f2.write(new_low)
    os.remove(path)
    os.rename(path + '.bat',path)

func('alex自述','太白','alex')
