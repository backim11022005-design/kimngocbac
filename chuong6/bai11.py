n = int(input("Nhập n: "))
_list = ['apple', 'banana', 'cat', 'elephant']
_new = [x for x in _list if len(x) > n]
print(_new)