#完整的存储对象
import pickle  #通过pickle可以将任何纯python对象存储到一个文件中，并在存储后将其取回
import json

file = './saveObject.json'
f = open(file, 'wb')

listObj = ['天气', '日期', '交通']

pickle.dump(listObj, f)
f.close()

import json
# outfile = open('saveData.json', 'w')
# outfile = open('saveData.json', 'w',encoding='utf-8')
with open('saveData.json', 'w') as outfile:
    json.dump(listObj, outfile, ensure_ascii=False)#支持中文写入
