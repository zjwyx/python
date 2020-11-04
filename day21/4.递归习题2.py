import os
def dir_size(path):
    size = 0
    name_list = os.listdir(path)
    for name in name_list:
        abs_path = os.path.join(path,name)
        if os.path.isfile(abs_path):
            size += os.path.getsize(abs_path)
        else:
            dir_size(abs_path)
    print(path,size)

dir_size('F:\python')




def menu_func(menu):
    flag = True
    while 1:
        for name in menu:
            print(name)
        key = input('>>>').strip()
        if menu.get(key):
            dic = menu[key]
            flag = menu_func(dic)

        elif key.upper() == 'B':
            return True
        elif key.upper() == 'Q':
            return False



menu_func(5)


