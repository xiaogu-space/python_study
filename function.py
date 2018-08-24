def sayHellow(aa):
    print(aa)


sayHellow('你好')

x = 50
y = 50


def fuc():
    x = 2
    global y

    y = 2
    print(x)
    print(y)


fuc()
print(x)
print(y)


def say(msg, times=3):  #赋值的参数必须位于后面
    print(msg * times)


say('你好', 1)
say('你好')


def setNum(a, b=5, c=10):  #指定参数赋值
    print('a=', a, 'b=', b, 'c=', c)


setNum(1, c=5)
