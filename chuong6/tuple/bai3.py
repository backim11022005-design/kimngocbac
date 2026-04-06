_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
temp_list = []
for x in _tuple:
    if x not in temp_list:
        temp_list.append(x)
_new_tuple = tuple(temp_list)
print(_new_tuple)