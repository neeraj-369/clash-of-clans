import math
from colorama import Fore, Back, Style
from time import sleep, time


class cannon:
    def __init__(self, values):
        for i in range(0, values.numberofcannons):
            x = values.cannons[i][0]
            y = values.cannons[i][1]
            values.frame[x][y] = values.cannon_symbol
            l = [y, x]
            values.available.remove(l)
            values.object_near[x][y] = 'cannon{}'.format(i+1)

    def cannon_hit(self, values):
        for i in range(0, values.numberofcannons):
            dist = 10000
            symbol = 'none'
            sy = 'troop'
            if(values.korq == 'k'):
                if(values.king_alive == 1):
                    dist = math.sqrt(
                        (values.king_x - values.cannons[i][0])**2 + (values.king_y - values.cannons[i][1])**2)
                    symbol = 'king'
            if(values.korq == 'q'):
                if(values.queen_alive == 1):
                    dist = math.sqrt(
                        (values.queen_x - values.cannons[i][0])**2 + (values.queen_y - values.cannons[i][1])**2)
                    symbol = 'queen'

            for j in range(0, values.barbarian_count):
                if(values.troop_alive[j] == 1 and values.troop[j] != 0):
                    can = math.sqrt(
                        (values.troops[j][0] - values.cannons[i][0])**2 + (values.troops[j][1] - values.cannons[i][1])**2)
                    if(can < dist):
                        dist = can
                        symbol = j

            for j in range(0, values.archer_count):
                if(values.archer_alive[j] == 1 and values.archer[j] != 0):
                    can = math.sqrt(
                        (values.archers[j][0] - values.cannons[i][0])**2 + (values.archers[j][1] - values.cannons[i][1])**2)
                    if(can < dist):
                        dist = can
                        symbol = j
                        sy = 'archer'

            if(dist <= 6 and values.cannon_alive[i] == 1):
                if(time() - values.tic[i] >= values.cannon_timestep):
                    values.tic[i] = time()
                    x = values.cannons[i][0]
                    y = values.cannons[i][1]
                    if(values.cannon_health[i] >= 50):
                        values.frame[x][y] = f"{Fore.GREEN}{Back.GREEN}{Style.BRIGHT} {Style.RESET_ALL}"

                    elif(values.cannon_health[i] >= 20 and values.cannon_health[i] < 50):
                        values.frame[x][y] = f"{Fore.YELLOW}{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"

                    elif(values.cannon_health[i] > 0 and values.cannon_health[i] < 20):
                        values.frame[x][y] = f"{Fore.RED}{Back.RED}{Style.BRIGHT} {Style.RESET_ALL}"

                    if(symbol == 'king'):
                        if(values.percentage >= 0):
                            values.percentage = values.percentage - values.cannon_hit
                        if(values.percentage < 0):
                            values.percentage = 0
                            values.king_alive = 0
                            values.frame[values.king_x][values.king_y] = " "

                    elif(symbol == 'queen'):
                        if(values.percentage >= 0):
                            values.percentage = values.percentage - values.cannon_hit
                        if(values.percentage < 0):
                            values.percentage = 0
                            values.queen_alive = 0
                            values.frame[values.queen_x][values.queen_y] = " "

                    elif (symbol != 'none' and sy == 'troop'):
                        if(values.troop_health[symbol] >= 0):
                            values.troop_health[symbol] = values.troop_health[symbol] - \
                                values.cannon_hit
                        if(values.troop_health[symbol] < 0):
                            values.troop_health[symbol] = 0
                            values.troop_alive[symbol] = 0
                            values.frame[values.troops[symbol][0]
                                         ][values.troops[symbol][1]] = " "

                    elif (symbol != 'none' and sy == 'archer'):
                        if(values.archer_health[symbol] >= 0):
                            values.archer_health[symbol] = values.archer_health[symbol] - \
                                values.cannon_hit
                        if(values.archer_health[symbol] < 0):
                            values.archer_health[symbol] = 0
                            values.archer_alive[symbol] = 0
                            values.frame[values.archers[symbol][0]
                                         ][values.archers[symbol][1]] = " "

                else:
                    if(values.cannon_health[i] > 0):
                        self.cannon_damage(i, values)
            else:
                x = values.cannons[i][0]
                y = values.cannons[i][1]
                if(values.cannon_health[i] > 0):
                    self.cannon_damage(i, values)

    def cannon_damage(self, i, values):

        if(values.cannon_health[i] >= 50):
            x = values.cannons[i][0]
            y = values.cannons[i][1]
            values.frame[x][y] = f"{Fore.BLUE}{Back.GREEN}{Style.BRIGHT}▣{Style.RESET_ALL}"

        elif(values.cannon_health[i] >= 20 and values.cannon_health[i] < 50):
            x = values.cannons[i][0]
            y = values.cannons[i][1]
            values.frame[x][y] = f"{Fore.BLUE}{Back.YELLOW}{Style.BRIGHT}▣{Style.RESET_ALL}"

        elif(values.cannon_health[i] > 0 and values.cannon_health[i] < 20):
            x = values.cannons[i][0]
            y = values.cannons[i][1]
            values.frame[x][y] = f"{Fore.BLUE}{Back.RED}{Style.BRIGHT}▣{Style.RESET_ALL}"

        elif(values.cannon_health[i] <= 0):
            x = values.cannons[i][0]
            y = values.cannons[i][1]
            values.frame[x][y] = " "
            l = [y, x]
            if l in values.available:
                s = 1
            else:
                values.available.append(l)
            values.object_near[x][y] = " "
            values.cannon_alive[i] = 0
