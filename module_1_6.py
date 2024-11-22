my_dict = {'Kate': 2000, 'Jack': 2001, 'Ron': 2005}
print(my_dict)
print(my_dict['Kate'])
print(my_dict.get('John', 'Такого имени нет'))
my_dict.update({'Kira': 1998,
                'L': 1999})
L = my_dict.pop('L')
print(L)
print(my_dict)

my_set = {1, 2, 'ok', (3, 4), 1, 2, 'ok', (3, 4)}
print(my_set)
my_set.add(5)
my_set.add((6, 7))
my_set.discard('ok')
print(my_set)