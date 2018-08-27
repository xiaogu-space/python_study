#捕获异常
#coding=utf-8
try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
except:  #不写具体的错误，但是必须写在最后
    print('我出错了')
else:  #没有发生异常时执行
    print('You entered {}'.format(text))