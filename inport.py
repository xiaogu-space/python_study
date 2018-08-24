# 能够接受输入的指令
import sys
import insayHi

for i in sys.argv:
    print(i)

insayHi.sayHi("你好")

insayHi.plus(1, 1)

print(dir(insayHi))  #打印出所有的名称
