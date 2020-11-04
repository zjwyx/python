import shutil

# 拷贝
# shutil.copy2('原文件','现文件')
# shutil.copy2('F:\python\day21\lianjia.html','F:\python\day21\lianjia_bk.html')


# shutil.copytree('outer',
#                 'outer2',
#                 ignore=shutil.ignore_patterns('__init__.py'))



# 删除
# shutil.rmtree('F:\python\day21\outer2',ignore_errors=True)


# 移动文件
# shutil.move('F:\python\day20','F:\python\day21\day20_back',copy_function=shutil.copy2())


# 获得磁盘的使用空间
# total, used, free = shutil.disk_usage(".")
# print("当前磁盘共: %iGB, 已使用: %iGB, 剩余: %iGB"%(total / 1073741824, used / 1073741824, free / 1073741824))


# 压缩文件
# shutil.make_archive('outer', 'zip','F:\python\day21\outer')

# 解压文件
# shutil.unpack_archive('outer.zip')
