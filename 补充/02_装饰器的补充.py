
def warrp(f):
    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret
    return inner

# index = warrp(index)
@warrp
def index(x,y):
    print(x,y)

index()  
# 偷梁换柱，即将原函数名指向的内存地址偷梁换柱成warrp函数
# 所有应该将warrp做的跟原函数一样才行