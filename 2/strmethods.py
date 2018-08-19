name = 'rutuja'

if name.startswith('rut'):
    print('Yes, the string starts with "rut"')

if 'u' in name:
    print('Yes, it contains the string "u"')

if name.find('ja') != -1:
    print('Yes, it contains the string "ja"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
