# 元组，元组内的数值不会改变
zoo = ('js', 'python', 'java')
zoo1 = ('js', )  #只有一个必须以','结尾
print('长度是：', len(zoo))


# 返回多个值会用到
def getErrorDetails():
    return (2, 'detail')


aa, bb = getErrorDetails()
print('aa:{},bb:{}'.format(aa, bb))
