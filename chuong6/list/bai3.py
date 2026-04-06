_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chan = [x for x in _list if x % 2 == 0]
le = [x for x in _list if x % 2 != 0]
print("List chẵn:", chan)
print("List lẻ:", le)