import math
from colorama import Fore, Back, Style
from time import sleep, time


class wizzard:
    def __init__(self, values):
        for i in range(0, values.numberofwizzards):
            x = values.wizzards[i][0]
            y = values.wizzards[i][1]
            values.frame[x][y] = values.wizzard_symbol
            l = [y, x]
            values.available.remove(l)
            values.object_near[x][y] = 'wizzard{}'.format(i+1)

    def wizzard_hit(self, values):
        for i in range(0, values.numberofwizzards):
            dist = 10000
            symbol = 'none'
            sy = 'troop'
            if(values.korq == 'k'):
                if(values.king_alive == 1):
                    dist = math.sqrt(
                        (values.king_x - values.wizzards[i][0])**2 + (values.king_y - values.wizzards[i][1])**2)
                    symbol = 'king'
            if(values.korq == 'q'):
                if(values.queen_alive == 1):
                    dist = math.sqrt(
                        (values.queen_x - values.wizzards[i][0])**2 + (values.queen_y - values.wizzards[i][1])**2)
                    symbol = 'queen'

            for j in range(0, values.barbarian_count):
                if(values.troop_alive[j] == 1 and values.troop[j] != 0):
                    can = math.sqrt(
                        (values.troops[j][0] - values.wizzards[i][0])**2 + (values.troops[j][1] - values.wizzards[i][1])**2)
                    if(can < dist):
                        dist = can
                        symbol = j

            for j in range(0, values.archer_count):
                if(values.archer_alive[j] == 1 and values.archer[j] != 0):
                    can = math.sqrt(
                        (values.archers[j][0] - values.wizzards[i][0])**2 + (values.archers[j][1] - values.wizzards[i][1])**2)
                    if(can < dist):
                        dist = can
                        symbol = j
                        sy = 'archer'

            for j in range(0, values.balloon_count):
                if(values.balloon_alive[j] == 1 and values.balloon[j] != 0):
                    can = math.sqrt(
                        (values.balloons[j][0] - values.wizzards[i][0])**2 + (values.balloons[j][1] - values.wizzards[i][1])**2)
                    if(can < dist):
                        dist = can
                        symbol = j
                        sy = 'balloon'

            if(dist <= 6 and values.wizzard_alive[i] == 1):
                if(time() - values.tici[i] >= values.wizzard_timestep):
                    values.tici[i] = time()
                    x = values.wizzards[i][0]
                    y = values.wizzards[i][1]
                    if(values.wizzard_health[i] >= 50):
                        values.frame[x][y] = f"{Fore.GREEN}{Back.GREEN}{Style.BRIGHT} {Style.RESET_ALL}"

                    elif(values.wizzard_health[i] >= 20 and values.wizzard_health[i] < 50):
                        values.frame[x][y] = f"{Fore.YELLOW}{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"

                    elif(values.wizzard_health[i] > 0 and values.wizzard_health[i] < 20):
                        values.frame[x][y] = f"{Fore.RED}{Back.RED}{Style.BRIGHT} {Style.RESET_ALL}"

                    if(symbol == 'king'):
                        if(values.percentage >= 0):
                            for i in range(values.king_x-1, values.king_x+2):
                                for j in range(values.king_y-1, values.king_y+2):
                                    if(i > 0 and i < 49 and j > 0 and j < 139):
                                        for k in range(0, values.archer_count):
                                            if(values.archers[k][0] == i and values.archers[k][1] == j):
                                                if(values.archer_health[k] >= 0):
                                                    values.archer_health[k] = values.archer_health[k] - \
                                                        values.wizzard_hit
                                                if(values.archer_health[k] < 0):
                                                    values.archer_health[k] = 0
                                                    values.archer_alive[k] = 0
                                                    values.frame[values.archers[k][0]
                                                                 ][values.archers[k][1]] = " "
                                        for k in range(0, values.balloon_count):
                                            if(values.balloons[k][0] == i and values.balloons[k][1] == j):
                                                if(values.balloon_health[k] >= 0):
                                                    values.balloon_health[k] = values.balloon_health[k] - \
                                                        values.wizzard_hit
                                                if(values.balloon_health[k] < 0):
                                                    values.balloon_health[k] = 0
                                                    values.balloon_alive[k] = 0
                                                    values.frame[values.balloons[k][0]
                                                                 ][values.balloons[k][1]] = " "
                                        for k in range(0, values.barbarian_count):
                                            if(values.troops[k][0] == i and values.troops[k][1] == j):
                                                if(values.troop_health[k] >= 0):
                                                    values.troop_health[k] = values.troop_health[k] - \
                                                        values.wizzard_hit
                                                if(values.troop_health[k] < 0):
                                                    values.troop_health[k] = 0
                                                    values.troop_alive[k] = 0
                                                    values.frame[values.troops[k][0]
                                                                 ][values.troops[k][1]] = " "
                                        if(values.korq == 'k'):
                                            if(values.king_x == i and values.king_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.king_alive = 0
                                                    values.frame[values.king_x][values.king_y] = " "
                                        if(values.korq == 'q'):
                                            if(values.queen_x == i and values.queen_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.queen_alive = 0
                                                    values.frame[values.queen_x][values.queen_y] = " "

                    elif(symbol == 'queen'):
                        if(values.percentage >= 0):
                            for i in range(values.queen_x-1, values.queen_x+2):
                                for j in range(values.queen_y-1, values.queen_y+2):
                                    if(i > 0 and i < 49 and j > 0 and j < 139):
                                        for k in range(0, values.archer_count):
                                            if(values.archers[k][0] == i and values.archers[k][1] == j):
                                                if(values.archer_health[k] >= 0):
                                                    values.archer_health[k] = values.archer_health[k] - \
                                                        values.wizzard_hit
                                                if(values.archer_health[k] < 0):
                                                    values.archer_health[k] = 0
                                                    values.archer_alive[k] = 0
                                                    values.frame[values.archers[k][0]
                                                                 ][values.archers[k][1]] = " "
                                        for k in range(0, values.balloon_count):
                                            if(values.balloons[k][0] == i and values.balloons[k][1] == j):
                                                if(values.balloon_health[k] >= 0):
                                                    values.balloon_health[k] = values.balloon_health[k] - \
                                                        values.wizzard_hit
                                                if(values.balloon_health[k] < 0):
                                                    values.balloon_health[k] = 0
                                                    values.balloon_alive[k] = 0
                                                    values.frame[values.balloons[k][0]
                                                                 ][values.balloons[k][1]] = " "
                                        for k in range(0, values.barbarian_count):
                                            if(values.troops[k][0] == i and values.troops[k][1] == j):
                                                if(values.troop_health[k] >= 0):
                                                    values.troop_health[k] = values.troop_health[k] - \
                                                        values.wizzard_hit
                                                if(values.troop_health[k] < 0):
                                                    values.troop_health[k] = 0
                                                    values.troop_alive[k] = 0
                                                    values.frame[values.troops[k][0]
                                                                 ][values.troops[k][1]] = " "
                                        if(values.korq == 'k'):
                                            if(values.king_x == i and values.king_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.king_alive = 0
                                                    values.frame[values.king_x][values.king_y] = " "
                                        if(values.korq == 'q'):
                                            if(values.queen_x == i and values.queen_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.queen_alive = 0
                                                    values.frame[values.queen_x][values.queen_y] = " "

                    elif (symbol != 'none' and sy == 'troop'):
                        if(values.troop_health[symbol] >= 0):
                            for i in range(values.troops[symbol][0]-1, values.troops[symbol][0]+2):
                                for j in range(values.troops[symbol][1]-1, values.troops[symbol][1]+2):
                                    if(i > 0 and i < 49 and j > 0 and j < 139):
                                        for k in range(0, values.archer_count):
                                            if(values.archers[k][0] == i and values.archers[k][1] == j):
                                                if(values.archer_health[k] >= 0):
                                                    values.archer_health[k] = values.archer_health[k] - \
                                                        values.wizzard_hit
                                                if(values.archer_health[k] < 0):
                                                    values.archer_health[k] = 0
                                                    values.archer_alive[k] = 0
                                                    values.frame[values.archers[k][0]
                                                                 ][values.archers[k][1]] = " "
                                        for k in range(0, values.balloon_count):
                                            if(values.balloons[k][0] == i and values.balloons[k][1] == j):
                                                if(values.balloon_health[k] >= 0):
                                                    values.balloon_health[k] = values.balloon_health[k] - \
                                                        values.wizzard_hit
                                                if(values.balloon_health[k] < 0):
                                                    values.balloon_health[k] = 0
                                                    values.balloon_alive[k] = 0
                                                    values.frame[values.balloons[k][0]
                                                                 ][values.balloons[k][1]] = " "
                                        for k in range(0, values.barbarian_count):
                                            if(values.troops[k][0] == i and values.troops[k][1] == j):
                                                if(values.troop_health[k] >= 0):
                                                    values.troop_health[k] = values.troop_health[k] - \
                                                        values.wizzard_hit
                                                if(values.troop_health[k] < 0):
                                                    values.troop_health[k] = 0
                                                    values.troop_alive[k] = 0
                                                    values.frame[values.troops[k][0]
                                                                 ][values.troops[k][1]] = " "
                                        if(values.korq == 'k'):
                                            if(values.king_x == i and values.king_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.king_alive = 0
                                                    values.frame[values.king_x][values.king_y] = " "
                                        if(values.korq == 'q'):
                                            if(values.queen_x == i and values.queen_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.queen_alive = 0
                                                    values.frame[values.queen_x][values.queen_y] = " "

                    elif (symbol != 'none' and sy == 'archer'):
                        if(values.archer_health[symbol] >= 0):

                            for i in range(values.archers[symbol][0]-1, values.archers[symbol][0]+2):
                                for j in range(values.archers[symbol][1]-1, values.archers[symbol][1]+2):
                                    if(i > 0 and i < 49 and j > 0 and j < 139):
                                        for k in range(0, values.archer_count):
                                            if(values.archers[k][0] == i and values.archers[k][1] == j):
                                                if(values.archer_health[k] >= 0):
                                                    values.archer_health[k] = values.archer_health[k] - \
                                                        values.wizzard_hit
                                                if(values.archer_health[k] < 0):
                                                    values.archer_health[k] = 0
                                                    values.archer_alive[k] = 0
                                                    values.frame[values.archers[k][0]
                                                                 ][values.archers[k][1]] = " "
                                        for k in range(0, values.balloon_count):
                                            if(values.balloons[k][0] == i and values.balloons[k][1] == j):
                                                if(values.balloon_health[k] >= 0):
                                                    values.balloon_health[k] = values.balloon_health[k] - \
                                                        values.wizzard_hit
                                                if(values.balloon_health[k] < 0):
                                                    values.balloon_health[k] = 0
                                                    values.balloon_alive[k] = 0
                                                    values.frame[values.balloons[k][0]
                                                                 ][values.balloons[k][1]] = " "
                                        for k in range(0, values.barbarian_count):
                                            if(values.troops[k][0] == i and values.troops[k][1] == j):
                                                if(values.troop_health[k] >= 0):
                                                    values.troop_health[k] = values.troop_health[k] - \
                                                        values.wizzard_hit
                                                if(values.troop_health[k] < 0):
                                                    values.troop_health[k] = 0
                                                    values.troop_alive[k] = 0
                                                    values.frame[values.troops[k][0]
                                                                 ][values.troops[k][1]] = " "
                                        if(values.korq == 'k'):
                                            if(values.king_x == i and values.king_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.king_alive = 0
                                                    values.frame[values.king_x][values.king_y] = " "
                                        if(values.korq == 'q'):
                                            if(values.queen_x == i and values.queen_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.queen_alive = 0
                                                    values.frame[values.queen_x][values.queen_y] = " "

                    elif (symbol != 'none' and sy == 'balloon'):
                        if(values.balloon_health[symbol] >= 0):
                            for i in range(values.balloons[symbol][0]-1, values.balloons[symbol][0]+2):
                                for j in range(values.balloons[symbol][1]-1, values.balloons[symbol][1]+2):
                                    if(i > 0 and i < 49 and j > 0 and j < 139):
                                        for k in range(0, values.archer_count):
                                            if(values.archers[k][0] == i and values.archers[k][1] == j):
                                                if(values.archer_health[k] >= 0):
                                                    values.archer_health[k] = values.archer_health[k] - \
                                                        values.wizzard_hit
                                                if(values.archer_health[k] < 0):
                                                    values.archer_health[k] = 0
                                                    values.archer_alive[k] = 0
                                                    values.frame[values.archers[k][0]
                                                                 ][values.archers[k][1]] = " "
                                        for k in range(0, values.balloon_count):
                                            if(values.balloons[k][0] == i and values.balloons[k][1] == j):
                                                if(values.balloon_health[k] >= 0):
                                                    values.balloon_health[k] = values.balloon_health[k] - \
                                                        values.wizzard_hit
                                                if(values.balloon_health[k] < 0):
                                                    values.balloon_health[k] = 0
                                                    values.balloon_alive[k] = 0
                                                    values.frame[values.balloons[k][0]
                                                                 ][values.balloons[k][1]] = " "
                                        for k in range(0, values.barbarian_count):
                                            if(values.troops[k][0] == i and values.troops[k][1] == j):
                                                if(values.troop_health[k] >= 0):
                                                    values.troop_health[k] = values.troop_health[k] - \
                                                        values.wizzard_hit
                                                if(values.troop_health[k] < 0):
                                                    values.troop_health[k] = 0
                                                    values.troop_alive[k] = 0
                                                    values.frame[values.troops[k][0]
                                                                 ][values.troops[k][1]] = " "
                                        if(values.korq == 'k'):
                                            if(values.king_x == i and values.king_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.king_alive = 0
                                                    values.frame[values.king_x][values.king_y] = " "
                                        if(values.korq == 'q'):
                                            if(values.queen_x == i and values.queen_y == j):
                                                if(values.percentage >= 0):
                                                    values.percentage = values.percentage - values.wizzard_hit
                                                if(values.percentage < 0):
                                                    values.percentage = 0
                                                    values.queen_alive = 0
                                                    values.frame[values.queen_x][values.queen_y] = " "

                else:
                    if(values.wizzard_health[i] > 0):
                        self.wizzard_damage(i, values)
            else:
                x = values.wizzards[i][0]
                y = values.wizzards[i][1]
                if(values.wizzard_health[i] > 0):
                    self.wizzard_damage(i, values)

    def wizzard_damage(self, i, values):

        if(values.wizzard_health[i] >= 50):
            x = values.wizzards[i][0]
            y = values.wizzards[i][1]
            values.frame[x][y] = f"{Fore.BLUE}{Back.GREEN}{Style.BRIGHT}w{Style.RESET_ALL}"

        elif(values.wizzard_health[i] >= 20 and values.wizzard_health[i] < 50):
            x = values.wizzards[i][0]
            y = values.wizzards[i][1]
            values.frame[x][y] = f"{Fore.BLUE}{Back.YELLOW}{Style.BRIGHT}w{Style.RESET_ALL}"

        elif(values.wizzard_health[i] > 0 and values.wizzard_health[i] < 20):
            x = values.wizzards[i][0]
            y = values.wizzards[i][1]
            values.frame[x][y] = f"{Fore.BLUE}{Back.RED}{Style.BRIGHT}w{Style.RESET_ALL}"

        elif(values.wizzard_health[i] <= 0):
            x = values.wizzards[i][0]
            y = values.wizzards[i][1]
            values.frame[x][y] = " "
            l = [y, x]
            if l in values.available:
                s = 1
            else:
                values.available.append(l)
            values.object_near[x][y] = " "
            values.wizzard_alive[i] = 0
