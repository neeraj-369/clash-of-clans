import signal
import tty
import os
import termios
import sys
from time import time


def timeout_handler():
    raise TimeoutError


class input_timer:

    def input_timer(self, values):
        ch = ""
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, values.timestep)
        try:
            mode = termios.tcgetattr(0)
            tty.setraw(0)
            ch = sys.stdin.read(1)
            signal.alarm(0)
        except:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
        termios.tcsetattr(0, termios.TCSADRAIN, mode)
        self.symbol = ch
