#基本结构
'''
while 条件
    循环体

1.先判断条件是否是true
2.如果是true进入循环体
3.执行到循环体的底部
4.继续判断条件，条件成立，进入循环体
'''

# 初识
# while True:
#     print('我们不一样');
#     print('狼的诱惑');
#     print('月亮之上');
#     print('人间');



# 循环如何终止
# flag = True
# while flag:
#     print('我们不一样');
#     print('狼的诱惑');
#     print('月亮之上');
#     flag = False
#     print('人间');

# 练习题 1-100多有的数字
# count = 1
# flag = True
# while flag:
#     print(count)
#     count = count + 1;
#     if count == 101 :
#         flag = False

# count = 1
# while count <= 100:
#     print(count);
#     count = count + 1

# 1-100的和
# count = 1
# sum = 0;
# while count <= 100:
#     sum += count;
#     count = count + 1;
# print(sum)


# break:循环中遇到break直接退出循环
# while True:
#     print('我们不一样');
#     print('狼的诱惑');
#     break;
#     print('月亮之上');
#     print('人间');

# 1-100所有的偶数的和
# count = 1
# sum = 0;
# while count <= 100:
#     if count % 2 == 0 :
#         sum += count
#     count = count + 1
# print(sum)


# continue : 退出本次循环，继续下次循环
# flag = True
# while flag:
#     print(111);
#     print(222);
#     flag = False;
#     continue;
#     print(333)



# flag = True
# while flag:
#     print(111);
#     print(222);
#     flag = False;
#     print(333)

# aaa = 1
# while aaa < 101:
#     print(aaa)
#     aaa += 1


# count = 1;
# sum = 0;
# while count < 101:
#     sum += count;
#     count += 1;
# print(sum)

count = 1
sum = 0
while True:
    sum += count;
    count +=1;
    if count == 101:
        break;
print(sum)