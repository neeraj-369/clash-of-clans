from src.values import values
from time import time


class statusbar:
    print("count  = {}".format(values.counter), end=" ")
    print("time = {}".format(int(time() - values.start_time)))
