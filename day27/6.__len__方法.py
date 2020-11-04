class Cls:
    def __init__(self,name):
        self.name = name
        self.students = []

    def __len__(self):
        return len(self.students)

py22 = Cls('py22')
py22.students.append('alex')
py22.students.append('大壮')
py22.students.append('台牌')
print(len(py22))




# class Pow:
#     def __init__(self,n):
#         self.n = n
#     def __pow2__(self):
#         return self.n**2
#
# def pow2(obj):
#     return obj.__pow2__()
#
# obj = Cls(10)
