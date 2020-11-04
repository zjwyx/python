'''
random模块的演示
'''

import random
# 获取[0,0,1,0)范围内的浮点数
# print(random.random())

# 获取[a,b)范围内的整数
# print(random.randint(3,10))

# 获取[a,b)范围内的浮点数
# print(random.uniform(3,10))

# 把参数指定的数据中的元素打乱，参数必须是一个可变的数据类型
# l1 = [i for i in range(10)]
# random.shuffle(l1)
# print(l1)

# 从x中随机抽取k个数据，组成一个列表返回
t = (1,2,3)
let = random.sample(t,len(t))
print(let)
# 通过sample()变相实现打乱














# random.random() 获取[0,0,1,0)范围内的浮点数
# random.randint(a,b) 获取[a,b)范围内的整数
# random.uniform(a,b) 获取[a,b)范围内的浮点数
# random.shuffle(x) 把参数指定的数据中的元素打乱，参数必须是一个可变的数据类型
# random.sample(x，k) 从x中随机抽取k个数据，组成一个列表返回