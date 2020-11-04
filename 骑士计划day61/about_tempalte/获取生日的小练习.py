'''
输入出生年月日，计算一下出生了多久
'''

from dateutil import relativedelta
from datetime import datetime

if __name__ == '__main__':
    birthday_str = input('请输入你的出生年月(2000-12-01):').strip()

    birthday = datetime.strptime(birthday_str,'%Y-%m-%d')

    now = datetime.now()
    r = relativedelta.relativedelta(now , birthday)
    print(r)
    print('你出生了{obj.years}年{obj.months}月{obj.days}天'.format(obj = r))






