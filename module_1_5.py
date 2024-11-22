immutable_var = 1, 'string', True
print(immutable_var)
immutable_var[0] = 2        # Кортеж - неизменяемый объект
print(immutable_var)
mutable_list = [1, 2, 3]
mutable_list[0] = 0
print(mutable_list)