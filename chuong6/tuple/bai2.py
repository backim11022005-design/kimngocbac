_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
_new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)
print(_new_tuple)