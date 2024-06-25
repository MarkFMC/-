def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c = [1,2,3])
value_list = 1, 'tree', False
value_dict = {'a': 'car', 'b': True, 'c': 'list'}
print_params(*value_list)
print_params(**value_dict)
value_list_2 = 99, 'table'
print_params(*value_list_2, 42)