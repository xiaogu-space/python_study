# coding:utf-8

poen='''fdsafsadf
afsdasdfsadf'''

f=open('./fileString.text','w')
f.write(poen)
f.close()

# f=open('./fileSample.py')
f=open('./fileString.text')
while True:
    line=f.readline()
    if(len(line))==0:
        break
    print(line)
f.close()