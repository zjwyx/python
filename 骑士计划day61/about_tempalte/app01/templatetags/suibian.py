from django import template
from datetime import datetime

register = template.Library()

@register.filter()
def sb(value):
    return value + 'sb'


@register.filter(name='wrc')
def wrc_dsb(value):
    # 获取当前时间
    now_stamp = datetime.timestamp(datetime.now())
    # value的秒数
    value_stamp = datetime.timestamp(value)
    stamp_diff = now_stamp - value_stamp
    if stamp_diff < 60:
        return '{}秒之前发布'.format(int(stamp_diff))
    elif stamp_diff < 5*60:
        return '{}分钟之前发布'.format(int(stamp_diff//60))
    else:
        return '{}发布'.format(value.strftime('%Y-%m-%d %H:%M:%S'))



