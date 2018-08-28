#得到一个新的数组原数组保持不变
listone = [2, 3, 4]
listtow = [2 * i for i in listone if i > 2]
print(listone)
print(listtow)