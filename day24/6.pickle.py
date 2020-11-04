class Course:
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price

python = Course('python','6 moneth',21800)

import pickle

# with open('picelefile',mode='wb') as f:
#     pickle.dump(python,f)

# with open('picelefile',mode='rb') as f:
#     ret = pickle.load(f)
#     print(ret.__dict__)