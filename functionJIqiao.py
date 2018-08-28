#在函数中接收元组与字典
def powersum(power, *args):
    total = 0
    for i in args:
        # total =total+ pow(i, power)
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))

#args签名加了一个*，所有的其他参数都传递到args中，并作为一个元组予以存储
#如果采用的是**，则额外的参数都将视为字典
