import threading

def print_something(something):
    print(something)


# use daemon
# other thread will stop if main thread stops
t = threading.Thread(target=print_something, args=("hello",), daemon=True)
t.start()

print("thread started")

t.join()
