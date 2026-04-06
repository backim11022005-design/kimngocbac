_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_new = []
for x in _list:
    if x not in _new:
        _new.append(x)
print("Giữ lại 1 phần tử:", _new)