#用来判断是否包含
countrys = ['china', 'india', 'japanese']
bri = set(countrys)

print('china' in countrys)
print('china' in bri)

co=bri.copy()
del countrys[1]
countrys.remove('china')

countrys.append('english')

print(countrys)
print(co)
