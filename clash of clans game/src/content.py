import os
from src.values import values
from time import time
from colorama import Fore, Back, Style


class content:

    def status(self, values):
        os.system('tput reset')
        self.statusbar(values)
        self.frame(values)

    def statusbar(self, values):
        percent = ("{0:.1f}").format(values.percentage)
        filledLength = int(values.percentage_boxlength *
                           (values.percentage/100))
        bar = values.fill * filledLength + ' ' * \
            (values.percentage_boxlength - filledLength)
        time1 = str(int(time() - values.start_time))
        if(values.korq == 'k'):
            print(
                Back.BLUE + Fore.GREEN + Style.BRIGHT + (
                    '\n\n\tKING HEALTH: |' + bar + '|' + percent + '%' + '\t\t\t' + 'LEVEL: ' + str(values.leveli + 1) +
                    '\t\t\t\t\tTIME : ' + time1 + '\t\n'
                ) + Style.RESET_ALL
            )
        if(values.korq == 'q'):
            print(
                Back.BLUE + Fore.GREEN + Style.BRIGHT + (
                    '\n\nARCHER QUEEN HEALTH: |' + bar + '|' + percent + '%' + '\t\t\t' + 'LEVEL: ' + str(values.leveli + 1) +
                    '\t\t\t\t\tTIME : ' + time1 + '\t\n'
                ) + Style.RESET_ALL
            )

    def frame(self, values):
        for i in range(values.frame_height):
            print("".join(values.frame[i]))
