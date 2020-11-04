# # 作业：用函数完成登录注册功能以及购物车的功能
# # 1.启动程序，用户可以选择四个选项：登录，注册，购物，退出
# # 2.用户注册，用户名不能重复，注册成功之后，用户名密码记录到文件中，密码的长度不能超过14个字符
# #
# # 3.用户登录，用户名密码从文件中读取，进行三次验证，验证不成功则退出整个程序
# # 4.用户登录成功之后才能选择购物车功能进行购物，购物功能
#     # 购物要求：
#     # 1.将购物车封装到一个函数中
#     # 2.在上周的基础上，可以实现充值的扩展，以及其他相关扩展
#     # 3.用户选择退出购物车时，将以购物的商品记录到一个文件中，将未付钱的但加入购物车的商品记录到一个文件中
#     # 4每个用户专属两个文件，一个文件（文件名：登录的用户名_buy_goods）存储已购买的商品，另一个文件（文件名：登录的用户名_want_buy）
#     # 存储加入购物车的商品但没有购买的文件（升级功能）
#     # 5.给购物车增加两个功能：1.可查看已购买的商品，2.可查看上次退出时加入购物车未购买的商品（升级功能）
#     # 6.对于第五题的第二个功能可以进行购买商品并追加到已购买的文件中（升级功能）
# # 5.退出则是退出整个程序
#
#
# def register():
#     pass
#
# def login():
#     pass
#
# def quit_out():
#     pass
#
# def shopping_car():
#     pass
#
#
# choice_dict = {
#     1:register,
#     2:login,
#     3:shopping_car,
#     4:quit_out
#
# }
#
#
# while 1:
#     choice = input('''
#     1.注册
#     2.登录
#     3.购物
#     4.退出
#     ''')
#
#
#     '''
#         if choice == '1':
#         register()
#     elif choice == '2':
#         login()
#     '''
#
#     choice_dict[int(choice)]()













goods = [
    {'name':'电脑','price':1999},
    {'name':'鼠标','price':10},
    {'name':'游艇','price':20},
    {'name':'美女','price':998}
]

shopping_car = {}

while 1:
    money = input('请充值:').strip()
    if money.isdigit():
        money = int(money)
        break
    else:
        print('有非数字元素，重新输入')


# enumerate 可哈希的，比如：列表，字典
flag = True
while flag:
    print('所有商品展示如下：')
    for index,commodity_dict in enumerate(goods):
        print('{}\t{}\t{}'.format(index+1,commodity_dict['name'],commodity_dict['price']))

    print('n或N\t 购物车结算\nq或Q\t 退出程序')
    select_num = input('请输入您的选择：')
    if select_num.isdigit():
        select_num = int(select_num)
        if 0<select_num<len(goods):
            if (select_num-1) not in shopping_car:
                shopping_car[select_num-1] = {'name':goods[select_num-1]['name'],'price':goods[select_num-1]['price'],'amount':1}
            else:
                shopping_car[select_num-1]['amount'] += 1
            print('您成功将:商品为{},单价为{},数量为1添加到购物车'.format(shopping_car[select_num-1]['name'],shopping_car[select_num-1]['price']))

        else:
            print('您输入的超出范围')


    elif select_num.upper() == 'N':
        # print(shopping_car)
        while 1:
            total_price = 0
            print('您购物车的商品如下：')
            for ind,com_dict in shopping_car.items():
                print('商品序号：{},商品名称：{}，商品单价：{},商品数量：{}'.\
                      format(ind+1,shopping_car[ind]['name'],shopping_car[ind]['price'],shopping_car[ind]['amount']))
                total_price += shopping_car[ind]['price'] * shopping_car[ind]['amount']
            print('此次购物车所有的商品的总价：%s元' %(total_price))

            if money < total_price:
                # 可以扩展充值功能
                del_num = input('请选择需要删除的商品序号（默认每次数量减一）').strip()
                if del_num.isdigit():
                    del_num = int(del_num)
                    if (del_num - 1) in shopping_car:
                        shopping_car[del_num - 1]['amount'] -= 1
                        if shopping_car[del_num-1]['amount'] == 0:
                            shopping_car.pop(del_num-1,'无此key')

                    else:
                        print('您输入的超出范围')

                else:
                    print('您输入的有误，请重新输入')
            else:
                money -= total_price
                print('您已经成功购买了上面的所有商品，剩余 %s 元' % (money))
                flag = False
                break


    # 保留购物车未结算的商品，写入文件，以便后续在结算
    elif select_num.upper() == 'Q':
        break
    else:
        print('您输入的有误，请重新输入')

