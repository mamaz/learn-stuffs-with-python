# run_test.py
import time

time.sleep(1) # simulate fetch token
token = "blabla"

class QuictStartHttp:
    def do_thing(self):
        print(token)


if __name__ == "__main__":
    QuictStartHttp().do_thing()