# av_catalog = {
#     "欧美":{
#         "www.111.com":["很多免费的，世界最大的","质量一般"],
#         "www.2222.com":["很多免费的，也很大","质量比yourporn高点"],
#         "333.com":["多事多拍，高质量图片很多","资源不多，更新慢"],
#         "444.com":["质量很多，真的很多","全部收费，请绕开"],
#     },
#     "日韩":{
#         "tokyou-hot":["质量怎么不清楚，个人已经不喜欢日韩范了","vaerygood"],
#     },
#     "大陆":{
#         "1024":["全部都是免费，真好，好人一生平安","服务器在国外，慢"]
#     }
# }

# a，给此["很多免费的，世界最大的","质量一般"]列表第二个位置插入一个元素，"量很大"
# av_catalog["欧美"]["www.111.com"].insert(1,"量很大")
# print(av_catalog)
# b，["质量很多，真的很多","全部收费，请绕开"]列表的全部收费，请绕开"删除
# av_catalog["欧美"]["444.com"].pop(1)
# print(av_catalog)


goods = [
    {
        "name":"电脑",
        "price":1999
    },
    {
        "name":"鼠标",
        "price":10
    },
    {
        "name":"游艇",
        "price":20
    },
    {
        "name":"美女",
        "price":998
    }
]
# 要求：
# 1：页面显示
# 序号+ 商品名称 + 商品价格，如
# 1  电脑  1999
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提醒输入有误，并重新输入
# 4：用户输入q或 Q，退出程序
# enumerate() 里面放可迭代对象


while 1:
    for i in goods:
        print(goods.index(i)+1,i["name"],i["price"])

    number = input("请输入商品的编号:").strip()
    if number.isdigit():
        if 0 < int(number) <= len(goods):
            print(goods[int(number) - 1]["name"])
        else:
            print("超出范围")
    else:
        print("输入的编号有非数字元素，请重新输入")