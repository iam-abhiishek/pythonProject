# data = {}
# print(type(data))

data1 = {'JS':'Atom', 'Python':['Pycharm','Sublime'], 'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(data1['Python'])
print(data1['Python'][1])
print(data1.get('Java'))
print(data1['Java']['JEE'])