#coding:utf-8
import sys
import time
f = None
try:
    f = open('fileString.text')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()  #为了兼容在所有的地方都是一秒钟输出一个
        print('Press ctrl+c now')
        time.sleep(2)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")

with open('fileString.text') as f:
    for line in f:
        print(line, end='')
