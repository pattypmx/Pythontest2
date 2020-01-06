#输出：
#我的名字：小猫
#我的年龄：20
#我的身高：170.5
#是否是男性：false

#定义变量
my_name = '小猫'
my_age = 20
my_height = 170.5
is_man = False
isMan = 1

#输出
print('我的名字是:%s' % my_name)          #字符串%s--->str
print('我的年龄是：%d岁' % my_age)         #数字%d--->digit
print('我的身高是：%.2f' % my_height)       #小数点%fPython默认会保留小数点后6位，需要确定小数点位数，使用.位数f
print('是否是男性：%s' % is_man)          #布尔值%s
print('是否是男性：%d' % is_man)          #是否是男性：0、1表示时，使用%d


