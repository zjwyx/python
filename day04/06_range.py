# l1 = [1,2,3,"alex","太白"]
# print(len(l1))
#
# for i in range(len(l1)):
#     print(i)

# print(int((361 / 10)%10))

for i in range(100,1000):
    gewei = int(i % 10)
    shiwei = int((i / 10)%10)
    baiwei = int(i / 100)
    if pow(gewei,3) + pow(shiwei,3) + pow(baiwei,3) == i:
        print(i)
