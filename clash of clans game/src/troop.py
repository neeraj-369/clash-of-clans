import math
from colorama import Fore, Back, Style
from time import sleep, time


class troop:
    def spawn(self, values, symbol):
        if(symbol == 'f' or symbol == 'F'):
            if(values.barbarian_count < 6):
                values.troop_done[values.barbarian_count] = 1
                values.troop_alive[values.barbarian_count] = 1
                x = 2
                y = 85
                values.troops.append([x, y])
                values.frame[x][y] = values.troop_symbol
                values.troop[values.barbarian_count] = 1
                values.barbarian_count += 1

        if(symbol == 'g' or symbol == 'G'):
            if(values.barbarian_count < 6):
                values.troop_done[values.barbarian_count] = 1
                values.troop_alive[values.barbarian_count] = 1
                x = 25
                y = 8
                values.troops.append([x, y])
                values.frame[x][y] = values.troop_symbol
                values.troop[values.barbarian_count] = 1
                values.barbarian_count += 1

        if(symbol == 'h' or symbol == 'H'):
            if(values.barbarian_count < 6):
                values.troop_done[values.barbarian_count] = 1
                values.troop_alive[values.barbarian_count] = 1
                x = 25
                y = 130
                values.troops.append([x, y])
                values.frame[x][y] = values.troop_symbol
                values.troop[values.barbarian_count] = 1
                values.barbarian_count += 1

    def nearest(self, i, values):
        x = values.troops[i][0]
        y = values.troops[i][1]
        main_list = []
        min_dist = []
        for i in range(0, values.numberofhuts):

            a = values.hut[i][0]
            b = values.hut[i][1]
            l = [b, a]
            if l in values.available:
                s = 1
            else:
                list = []
                list.append([a, b])
                list.append([a+1, b])
                list.append([a, b+1])
                list.append([a+1, b+1])
                dist = []
                dist.append(math.sqrt((x-a)*(x-a)+(y-b)*(y-b)))
                dist.append(math.sqrt((x-a-1)*(x-a-1)+(y-b)*(y-b)))
                dist.append(math.sqrt((x-a)*(x-a)+(y-b-1)*(y-b-1)))
                dist.append(math.sqrt((x-a-1)*(x-a-1)+(y-b-1)*(y-b-1)))
                c = dist.index(min(dist))
                mina = min(dist)
                main_list.append(list[c])
                min_dist.append(mina)

        if(len(main_list) > 0):
            ind = min_dist.index(min(min_dist))
            nearest_hut = main_list[ind]

        cannon_list = []
        cannon_dist = 10000
        cannon_list.append(0)
        for i in range(0, values.numberofcannons):
            a = values.cannons[i][0]
            b = values.cannons[i][1]
            l = [b, a]
            if l in values.available:
                s = 1
            else:
                disto = math.sqrt((x-a)*(x-a)+(y-b)*(y-b))
                if(cannon_dist > disto):
                    cannon_dist = disto
                    cannon_list[0] = [a, b]

        for i in range(0, values.numberofwizzards):
            a = values.wizzards[i][0]
            b = values.wizzards[i][1]
            l = [b, a]
            if l in values.available:
                s = 1
            else:
                disto = math.sqrt((x-a)*(x-a)+(y-b)*(y-b))
                if(cannon_dist > disto):
                    cannon_dist = disto
                    cannon_list[0] = [a, b]
#################
        l = [values.townhall_x[0], values.townhall_y[0]]
        if l in values.available:
            b = 10000
        else:
            mini = 2000
            town_list = []
            dist_list = []
            for i in range(0, 4):
                a = values.townhall_y[0]
                b = values.townhall_y[3]
                dist1 = math.sqrt(
                    (a-x)**2 + (values.townhall_x[i]-y)**2)
                dist2 = math.sqrt(
                    (b-x)**2 + (values.townhall_x[i]-y)**2)
                if(dist1 < dist2):
                    dist = dist1
                else:
                    dist = dist2
                if(dist < mini):
                    mini = dist
                    town_list.append(0)
                    dist_list.append(0)
                    if(dist1 < dist2):
                        town_list[0] = [a, values.townhall_x[i]]
                    if(dist1 >= dist2):
                        town_list[0] = [b, values.townhall_x[i]]
                    dist_list[0] = dist

            #####################
            minii = 20000
            for i in range(0, 4):
                a = values.townhall_x[0]
                b = values.townhall_x[3]
                dist1 = math.sqrt(
                    (values.townhall_y[i]-x)**2 + (y-a)**2)
                dist2 = math.sqrt(
                    (values.townhall_y[i]-x)**2 + (y-b)**2)
                if(dist1 < dist2):
                    dist = dist1
                else:
                    dist = dist2

                if(dist < minii):
                    minii = dist
                    town_list.append(0)
                    dist_list.append(0)
                    if(dist1 < dist2):
                        town_list[1] = [values.townhall_y[i], a]
                    if(dist1 >= dist2):
                        town_list[1] = [values.townhall_y[i], b]
                    dist_list[1] = dist

            if(dist_list[0] < dist_list[1]):
                nearest_townhall = town_list[0]
            else:
                nearest_townhall = town_list[1]
            b = math.sqrt((nearest_townhall[0]-x)
                          ** 2 + (nearest_townhall[1]-y)**2)

        if(len(main_list) > 0):
            a = math.sqrt((nearest_hut[0]-x)**2 + (nearest_hut[1]-y)**2)
        else:
            a = 10000

        c = cannon_dist

        if(a < b):
            if(c < a):
                coordinates = cannon_list[0]
            else:
                coordinates = nearest_hut

        elif(a == b):
            if(c < a):
                coordinates = cannon_list[0]
            else:
                coordinates = -1
        else:
            if(c < b):
                coordinates = cannon_list[0]
            else:
                coordinates = [nearest_townhall[0], nearest_townhall[1]]

        return coordinates
        #######################

    def color(self, x, y, values, i):
        if(values.troop_health[i] >= 50):
            values.frame[x][y] = f"{Fore.GREEN}{Style.BRIGHT}♖{Style.RESET_ALL}"
        if(values.troop_health[i] >= 20 and values.troop_health[i] < 50):
            values.frame[x][y] = f"{Fore.YELLOW}{Style.BRIGHT}♖{Style.RESET_ALL}"
        if(values.troop_health[i] < 20):
            values.frame[x][y] = f"{Fore.RED}{Style.BRIGHT}♖{Style.RESET_ALL}"

    def automate(self, i, values, hut_1, hut_2, hut_3, hut_4, townhall, cannon, wizzard):
        coordinates = self.nearest(i, values)
        x = values.troops[i][0]
        y = values.troops[i][1]
        # values.frame[x][y] = values.troop_symbol
        self.color(x, y, values, i)
        if(coordinates != -1):

            if(coordinates[0] < x and coordinates[1] < y):
                l = [y-1, x-1]

                if l in values.available:
                    values.frame[x][y] = " "
                    # values.frame[x-1][y-1] = values.troop_symbol
                    self.color(x-1, y-1, values, i)
                    values.troops[i][0] = x-1
                    values.troops[i][1] = y-1

                else:
                    if (values.object_near[x-1][y-1] == 'wall'):

                        if (values.object_near[x-1][y-1] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x][y-1] = values.troop_symbol
                            self.color(x-1, y-1, values, i)
                            values.troops[i][0] = x-1
                            values.troops[i][1] = y-1
                            values.object_near[x-1][y-1] = " "


                            values.available.append([y-1, x-1])

                        elif (values.object_near[x-1][y] == 'wall'):

                            values.frame[x][y] = " "
                            # values.frame[x-1][y] = values.troop_symbol
                            self.color(x-1, y, values, i)
                            values.troops[i][0] = x-1
                            values.troops[i][1] = y
                            values.object_near[x-1][y] = " "
                            values.available.append([y, x-1])

                    if(values.object_near[x-1][y-1] == 'townhall' or values.object_near[x-1][y-1] == 'hut' or values.object_near[x-1][y-1] == 'cannon'):
                        values.frame[x][y] = " "
                        # values.frame[x][y-1] = values.troop_symbol
                        self.color(x, y-1, values, i)
                        values.troops[i][0] = x
                        values.troops[i][1] = y-1

            if(coordinates[0] < x and coordinates[1] > y):
                l = [y+1, x-1]
                if l in values.available:
                    values.frame[x][y] = " "
                    # values.frame[x-1][y+1] = values.troop_symbol
                    self.color(x-1, y+1, values, i)
                    values.troops[i][0] = x-1
                    values.troops[i][1] = y+1
                else:
                    if (values.object_near[x-1][y+1] == 'wall'):
                        if (values.object_near[x-1][y+1] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x][y+1] = values.troop_symbol
                            self.color(x-1, y+1, values, i)
                            values.troops[i][0] = x-1
                            values.troops[i][1] = y+1
                            values.object_near[x-1][y+1] = " "
                            values.available.append([y+1, x-1])

                        elif (values.object_near[x-1][y] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x-1][y] = values.troop_symbol
                            self.color(x-1, y, values, i)
                            values.troops[i][0] = x-1
                            values.troops[i][1] = y
                            values.object_near[x-1][y] = " "
                            values.available.append([y, x-1])

                    if(values.object_near[x-1][y+1] == 'townhall' or values.object_near[x-1][y+1] == 'hut' or values.object_near[x-1][y+1] == 'cannon'):
                        values.frame[x][y] = " "
                        # values.frame[x][y+1] = values.troop_symbol
                        self.color(x, y+1, values, i)
                        values.troops[i][0] = x
                        values.troops[i][1] = y+1

            if(coordinates[0] > x and coordinates[1] < y):
                l = [y-1, x+1]
                if l in values.available:
                    values.frame[x][y] = " "
                    # values.frame[x+1][y-1] = values.troop_symbol
                    self.color(x+1, y-1, values, i)
                    values.troops[i][0] = x+1
                    values.troops[i][1] = y-1
                else:
                    if (values.object_near[x+1][y-1] == 'wall'):
                        if (values.object_near[x+1][y-1] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x][y-1] = values.troop_symbol
                            self.color(x+1, y-1, values, i)
                            values.troops[i][0] = x+1
                            values.troops[i][1] = y-1
                            values.object_near[x+1][y-1] = " "
                            values.available.append([y-1, x+1])

                        elif (values.object_near[x+1][y] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x+1][y] = values.troop_symbol
                            self.color(x+1, y, values, i)
                            values.troops[i][0] = x-1
                            values.troops[i][1] = y
                            values.object_near[x+1][y] = " "
                            values.available.append([y, x+1])

                    if(values.object_near[x+1][y-1] == 'townhall' or values.object_near[x+1][y-1] == 'hut' or values.object_near[x+1][y-1] == 'cannon'):
                        values.frame[x][y] = " "
                        # values.frame[x][y-1] = values.troop_symbol
                        self.color(x, y-1, values, i)
                        values.troops[i][0] = x
                        values.troops[i][1] = y-1

            if(coordinates[0] > x and coordinates[1] > y):
                l = [y+1, x+1]
                if l in values.available:
                    values.frame[x][y] = " "
                    # values.frame[x+1][y+1] = values.troop_symbol
                    self.color(x+1, y+1, values, i)
                    values.troops[i][0] = x+1
                    values.troops[i][1] = y+1
                else:
                    if (values.object_near[x+1][y+1] == 'wall'):
                        if (values.object_near[x+1][y+1] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x][y+1] = values.troop_symbol
                            self.color(x+1, y+1, values, i)
                            values.troops[i][0] = x+1
                            values.troops[i][1] = y+1
                            values.object_near[x+1][y+1] = " "
                            values.available.append([y+1, x+1])

                        elif (values.object_near[x+1][y] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x+1][y] = values.troop_symbol
                            self.color(x+1, y, values, i)
                            values.troops[i][0] = x+1
                            values.troops[i][1] = y
                            values.object_near[x+1][y] = " "
                            values.available.append([y, x+1])

                    if(values.object_near[x+1][y+1] == 'townhall' or values.object_near[x+1][y+1] == 'hut' or values.object_near[x+1][y+1] == 'cannon'):
                        values.frame[x][y] = " "
                        # values.frame[x][y+1] = values.troop_symbol
                        self.color(x, y+1, values, i)
                        values.troops[i][0] = x
                        values.troops[i][1] = y+1

            if(coordinates[0] == x):
                if(coordinates[1] < y):
                    l = [y-1, x]
                    if l in values.available:
                        values.frame[x][y] = " "
                        # values.frame[x][y-1] = values.troop_symbol
                        self.color(x, y-1, values, i)
                        values.troops[i][0] = x
                        values.troops[i][1] = y-1
                    else:
                        if(values.object_near[x][y-1] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x][y-1] = values.troop_symbol
                            self.color(x, y-1, values, i)
                            values.troops[i][0] = x
                            values.troops[i][1] = y-1
                            values.object_near[x][y-1] = " "
                            values.available.append([y-1, x])
                        else:
                            value = values.object_near[x][y-1]
                            if(value[0:3] == 'hut'):
                                number = int(value[-1])-1
                                values.huts_health[number] = values.huts_health[number] - \
                                    values.troop_hit
                                if(value == 'hut1'):
                                    hut_1.hut_damage(values)
                                elif(value == 'hut2'):
                                    hut_2.hut_damage(values)
                                elif(value == 'hut3'):
                                    hut_3.hut_damage(values)
                                elif(value == 'hut4'):
                                    hut_4.hut_damage(values)
                            if(value == 'townhall'):
                                values.townhall_health = values.townhall_health-values.troop_hit
                                townhall.townhall_damage(values)
                            if(value[0:6] == 'cannon'):
                                number = int(value[-1])-1
                                values.cannon_health[number] = values.cannon_health[number] - \
                                    values.troop_hit
                                cannon.cannon_damage(number, values)

                            if(value[0:7] == 'wizzard'):
                                number = int(value[-1])-1
                                values.wizzard_health[number] = values.wizzard_health[number] - \
                                    values.archer_hit
                                wizzard.wizzard_damage(number, values)

                if(coordinates[1] > y):
                    l = [y+1, x]
                    if l in values.available:
                        values.frame[x][y] = " "
                        # values.frame[x][y+1] = values.troop_symbol
                        self.color(x, y+1, values, i)
                        values.troops[i][0] = x
                        values.troops[i][1] = y+1
                    else:
                        if(values.object_near[x][y+1] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x][y+1] = values.troop_symbol
                            self.color(x, y+1, values, i)
                            values.troops[i][0] = x
                            values.troops[i][1] = y+1
                            values.object_near[x][y+1] = " "
                            values.available.append([y+1, x])
                        else:
                            value = values.object_near[x][y+1]
                            if(value[0:3] == 'hut'):

                                number = int(value[-1])-1
                                values.huts_health[number] = values.huts_health[number] - \
                                    values.troop_hit
                                if(value == 'hut1'):
                                    hut_1.hut_damage(values)
                                elif(value == 'hut2'):
                                    hut_2.hut_damage(values)
                                elif(value == 'hut3'):
                                    hut_3.hut_damage(values)
                                elif(value == 'hut4'):
                                    hut_4.hut_damage(values)
                            if(value == 'townhall'):
                                values.townhall_health = values.townhall_health-values.troop_hit
                                townhall.townhall_damage(values)
                            if(value[0:6] == 'cannon'):
                                number = int(value[-1])-1
                                values.cannon_health[number] = values.cannon_health[number] - \
                                    values.troop_hit

                                cannon.cannon_damage(number, values)

                            if(value[0:7] == 'wizzard'):
                                number = int(value[-1])-1
                                values.wizzard_health[number] = values.wizzard_health[number] - \
                                    values.archer_hit
                                wizzard.wizzard_damage(number, values)

            elif(coordinates[1] == y):
                if(coordinates[0] < x):
                    l = [y, x-1]
                    if l in values.available:
                        values.frame[x][y] = " "
                        # values.frame[x-1][y] = values.troop_symbol
                        self.color(x-1, y, values, i)
                        values.troops[i][0] = x-1
                        values.troops[i][1] = y
                    else:
                        if(values.object_near[x-1][y] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x-1][y] = values.troop_symbol
                            self.color(x-1, y, values, i)
                            values.troops[i][0] = x-1
                            values.troops[i][1] = y
                            values.object_near[x-1][y] = " "
                            values.available.append([y, x-1])
                        else:
                            value = values.object_near[x-1][y]
                            if(value[0:3] == 'hut'):

                                number = int(value[-1])-1
                                values.huts_health[number] = values.huts_health[number] - \
                                    values.troop_hit
                                if(value == 'hut1'):
                                    hut_1.hut_damage(values)
                                elif(value == 'hut2'):
                                    hut_2.hut_damage(values)
                                elif(value == 'hut3'):
                                    hut_3.hut_damage(values)
                                elif(value == 'hut4'):
                                    hut_4.hut_damage(values)
                            if(value == 'townhall'):
                                values.townhall_health = values.townhall_health-values.troop_hit
                                townhall.townhall_damage(values)
                            if(value[0:6] == 'cannon'):
                                number = int(value[-1])-1
                                values.cannon_health[number] = values.cannon_health[number] - \
                                    values.troop_hit

                                cannon.cannon_damage(number, values)

                            if(value[0:7] == 'wizzard'):
                                number = int(value[-1])-1
                                values.wizzard_health[number] = values.wizzard_health[number] - \
                                    values.archer_hit

                                wizzard.wizzard_damage(number, values)

                if(coordinates[0] > x):
                    l = [y, x+1]
                    if l in values.available:
                        values.frame[x][y] = " "
                        # values.frame[x+1][y] = values.troop_symbol
                        self.color(x+1, y, values, i)
                        values.troops[i][0] = x+1
                        values.troops[i][1] = y
                    else:
                        if(values.object_near[x+1][y] == 'wall'):
                            values.frame[x][y] = " "
                            # values.frame[x+1][y] = values.troop_symbol
                            self.color(x+1, y, values, i)
                            values.troops[i][0] = x+1
                            values.troops[i][1] = y
                            values.object_near[x+1][y] = " "
                            values.available.append([y, x+1])
                        else:
                            value = values.object_near[x+1][y]
                            if(value[0:3] == 'hut'):

                                number = int(value[-1])-1
                                values.huts_health[number] = values.huts_health[number] - \
                                    values.troop_hit
                                if(value == 'hut1'):
                                    hut_1.hut_damage(values)
                                elif(value == 'hut2'):
                                    hut_2.hut_damage(values)
                                elif(value == 'hut3'):
                                    hut_3.hut_damage(values)
                                elif(value == 'hut4'):
                                    hut_4.hut_damage(values)
                            if(value == 'townhall'):
                                values.townhall_health = values.townhall_health-values.troop_hit
                                townhall.townhall_damage(values)
                            if(value[0:6] == 'cannon'):
                                number = int(value[-1])-1
                                values.cannon_health[number] = values.cannon_health[number] - \
                                    values.troop_hit

                                cannon.cannon_damage(number, values)

                            if(value[0:7] == 'wizzard'):
                                number = int(value[-1])-1
                                values.wizzard_health[number] = values.wizzard_health[number] - \
                                    values.archer_hit

                                wizzard.wizzard_damage(number, values)
