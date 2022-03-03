# testing CPU bound command
import time

COUNT=50000000

def countdown(num):
    n = num
    while n>=0:
        n-=1

start = time.time()
countdown(COUNT)
end = time.time()

print("Elapsed time: ", end - start)
