my_list = ('apple' , 'banana' , 'kiwi' , 'lemon')
print(my_list)
print('first element: ' + my_list[0])
print('last element: ' + my_list[-1])
print(my_list[2:5])
my_list = ('Modifie list:', ['apple' , 'banana' , 'orange' , 'lemon'])
print(my_list)

a = ('Dictionary: ')
my_dict = {'apple': 'яблоко' , 'banana': 'банан', 'lemon': 'лимон'}
print((a), (my_dict))
b = ('Translation: ')
print((b), (my_dict['lemon']))
c = ('Modified_dictionary:')
my_dict = {'apple': 'яблоко' ,
           'banana': 'банан',
           'lemon': 'лимон'}

del my_dict['lemon']
my_dict.update({'orange': 'апельсин'})

print((c), (my_dict))
