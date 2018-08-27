# 输入示例
#coding=utf-8
def reverse(text):
    t = text[::-1]  #顺序取反
    print('111:', t)
    return t


def is_palindrome(text):
    b = text == reverse(text)
    print('222:', b)
    return b


inString = input('输入信息：')

res = is_palindrome(inString)
print(res)
