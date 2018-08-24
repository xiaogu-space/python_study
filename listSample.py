# -*- coding: UTF-8 -*-
shopList = ['苹果', '香蕉', '鸭梨']
print('我有', len(shopList), '中水果要去买')

for item in shopList:
    print(item)
shopList.append('荔枝')
print(shopList)
shopList.sort()
print(shopList)

help(list)