# thread unsafe code without the GIL

import threading

x = []

def append_two(lst):
    lst.append(2)

th = threading.Thread(target=append_two, args=(x,))
th.start()

x.append(1)
print(x)
