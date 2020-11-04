# sys.argy练习
# 写一个python脚本，在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址

# import sys
# import os
# import shutil
#
# print(sys.argv)
# if len(sys.argv) >= 5:
#     if sys.argv[1] == 'alex' and sys.argv[2] == 'sb':
#         if sys.argv[3] == 'cp' and len(sys.argv) == 6:
#             if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
#                 filename = os.path.basename(sys.argv[4])
#                 path = os.path.join(sys.argv[5].filename)
#                 shutil.copy2(sys.argv[4],path)
#         elif sys.argv[3] == 'rm' and len(sys.argv) == 5:
#             if os.path.exists(sys.argv[4]):
#                 if os.path.isfile(sys.argv[4]):
#                     os.remove(sys.argv[4])
#                 else:
#                     shutil.rmtree(sys.argv[4])
#         elif sys.argv[3] == 'rename' and len(sys.argv) == 6:
#             if os.path.exists(sys.argv[4]):
#                 if os.path.isfile(sys.argv[4]):
#                     os.rename(sys.argv[4],sys.argv[5])
#                 else:
#                     shutil.move(sys.argv[4],sys.argv[5],copy_function=shutil.copy2)
# else:
#     print('您输入的命令无效')









# 使用walk来计算文件夹的总大小
# import os
# g = os.walk('F:\python')
# size = 0
# for i in g:
#     path,dir_lst,name_lst = i
#     for name in name_lst:
#         abs_path = os.path.join(path,name)
#         size += os.path.getsize(abs_path)
# print(size)
