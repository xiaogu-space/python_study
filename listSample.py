#coding=utf-8
shopList = ['苹果', '香蕉', '鸭梨']
print('我有', len(shopList), '中水果要去买')

for item in shopList:
    print(item)
shopList.append('荔枝')
print(shopList)
shopList.sort()
print(shopList)

del shopList[0]
print(shopList)

#字符串也一样
listNames = ['小明0', '小明1', '小明2', '小明3', '小明4', '小明5']
print('第0个', listNames[0])
print('第1~2个', listNames[1:3])
print('第2到最后', listNames[2:])
print('去掉最后一个',listNames[:-1])
print('得到全部的偶数',listNames[::2])
# help(list)