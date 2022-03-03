from random import randint
from multiprocessing import Manager, Process

def compute(results):
    results.append(sum([randint(1, 100) for _ in range(1000_000)]))

def run():
    with Manager() as manager:
        results = manager.list()
        workers = [Process(target=compute, args=(results,)) for x in range(8)]

        # starting
        for worker in workers:
            worker.start()

        # join makes workers result to be passed to main thread
        for worker in workers:
            worker.join()

        print('Results ', results)

if __name__ == "__main__":
    run()