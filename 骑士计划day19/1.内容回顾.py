
# 继承：提高代码的重用性，规范代码（要就继承父类的子类都实现相同的方法，抽象类，接口）
# 当你开始编写两个类的时候，出现了重复的代码，通过继承来简化代码，把重复的代码放在父类中
    # 单继承
        # 重用性：减少了代码的重复，子类可以重复用父类的方法
        # 派生：子类在父类的基础上又创建了自己的新的方法和属性
            # 子类中有父类的同名方法，只用子类的
                # 还希望用到父类中的方法，：父类名，super()调用
        # 抽象类：只能被继承，不能实例化，模板，规则
            # from abc import ABCMeta,abstractmethod
            # 在这个类创建的时候指定 metaclass=ABCMeta
            # 在你子类实现的方法上加上一个 @abstractmethod 装饰器

# from abc import ABCMeta,abstractmethod
# class A(metaclass=ABCMeta):
#     @abstractmethod
#     def func(self):
#         pass


    # 多继承
        # python,c++
        # java,c#
    # 每个类中有每个类能完成的方法
    # 创建子类的时候只需要挑选和找符合的父亲来继承就能够完成父类的功能了
    # 接口：java中的一种数据类型
    #
    # 经典类和新式类的区别
    # 经典类
        # 不主动继承object，没有mro方法，没有super，继承的时候，深度优先
    # 新式类
        # 主动继承object，有mro方法，有super，继承的时候，广度优先
