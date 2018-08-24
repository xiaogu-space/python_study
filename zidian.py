db = {'aaa': 'aaa', 'bbb': 'bbb', 'ccc': 'ccc'}
print(db)
print(db['aaa'])

for item in db.items():
    print(item)

for key, value in db.items():
    print('key:', key, 'value:', value)

del db['bbb']
print(db)
