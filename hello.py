# -*- coding: UTF-8 -*-
# 要想支持中文必须加上第一行
aa = 20
name = '小明'
print ('我是{0},今年{1}岁'.format(name, aa))  #好
print ('我是{},今年{}岁'.format(name, aa))  #好
print ('我是' + name + ',今年' + str(aa) + '岁')  #差
print ('我是' + name + ',今年' + str(aa) + '岁')  #

print ('a',end='')

print ('{0:.3f}'.format(1.0 / 3))  #保留三位小数
print ('{0:*^11}'.format('aaa'))  #保留11位，且aaa在中间
print ('{aaa}'.format(aaa='你好啊'))  #基于关键字
print ('{aaa}'.format(aaa=aa));
print ('小明说：\'你好\'')
print ('你好\
你好')#这是一行