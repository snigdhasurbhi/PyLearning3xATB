# dict orders are ramdom
# 1.7+ only
d = {'b': 1, 'a': 2, 'r': 3}
print(d)  # {'b': 1, 'a': 2, 'r': 3}
d = dict([('b', 1), ('a', 2), ('r', 3),('c',4),('ram',6)])
print(d)  # {'b': 1, 'a': 2, 'r': 3}

for k,v in d.items():
    print(k,v)
    print(f'{k}:{v}')
my_dict=dict()
my_dict['ram']=24
my_dict['shyam']=30
my_dict['radha']=26
my_dict['om']=27
my_dict['shiv']=28
my_dict['sankar']=29
print(my_dict)

from collections import OrderedDict
my_dict=OrderedDict()
my_dict['ram']=24
my_dict['shyam']=30
my_dict['radha']=26
my_dict['om']=27
my_dict['shiv']=28
my_dict['sankar']=29
print(my_dict)