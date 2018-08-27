#ecoding=utf-8
#抛出异常，通过raise语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出异常的对象


class shortInputException(Exception):
    '''一个由用户定义的异常类'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('请输入：')
    print(len(text))
    if len(text) < 3:
        raise shortInputException(len(text), 3)
except EOFError:
    print('why did you do an EOF on me')
except shortInputException as ex:
    print(('ShortInputException:The input was' +
           '{} long,expected at least {}'.format(ex.length, ex.atleast)))
except:
    print('异常了')
else:
    print('我是正确的')