dictionary = {1:'abhishek',2:'raaz',3:'correct'}
print(dictionary[1])
print(dictionary[3])
print(dictionary[2])
# print(dictionary[4])

print(dictionary.get(1))
print(dictionary.get(4,'not found'))

keys = [1, 2, 3]
values = ['hi', 'bye', 'chill']

data = dict(zip(keys,values))
print(data)

print(data[1])
print(data.get(2))

data['dance'] = 'New'
print(data)

data[5] = 'New'
print(data)

del data['dance']
print(data)

