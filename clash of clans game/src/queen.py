from colorama import Fore, Back, Style


class queen:
    def queen_hit(self, values, townhall, hut_1, hut_2, hut_3, hut_4, wall, cannon, wizzard):

        if(values.queen_alive == 1):
            hit_coordinates = [0, 0]
            if(values.queen_prev == 'w'):
                hit_coordinates[0] = values.queen_x - values.queen_range
                hit_coordinates[1] = values.queen_y
            if(values.queen_prev == 'a'):
                hit_coordinates[0] = values.queen_x
                hit_coordinates[1] = values.queen_y - values.queen_range
            if(values.queen_prev == 's'):
                hit_coordinates[0] = values.queen_x + values.queen_range
                hit_coordinates[1] = values.queen_y
            if(values.queen_prev == 'd'):
                hit_coordinates[0] = values.queen_x
                hit_coordinates[1] = values.queen_y + values.queen_range

            hit_available = []
            wall_available = []

            for i in range(hit_coordinates[0]-int(values.queen_side/2), hit_coordinates[0]+int(values.queen_side/2+1)):
                for j in range(hit_coordinates[1]-int(values.queen_side/2), hit_coordinates[1]+int(values.queen_side/2+1)):
                    if(i > 0 and i < 49 and j > 0 and j < 139):
                        if values.object_near[i][j] in hit_available and values.object_near[i][j] != "wall":
                            s = 1
                        else:
                            hit_available.append(values.object_near[i][j])
                            if(values.object_near[i][j] == "wall"):
                                l = [i, j]
                                wall_available.append(l)

            for str in hit_available:
                if(str != ' '):
                    if(str == "townhall"):
                        # exit(0)
                        values.townhall_health = values.townhall_health-values.queen_hit
                        townhall.townhall_damage(values)
                    if(str[0:3] == "hut"):
                        number = int(str[-1])-1
                        values.huts_health[number] = values.huts_health[number] - \
                            values.queen_hit
                        if(str == 'hut1'):
                            hut_1.hut_damage(values)
                        elif(str == 'hut2'):
                            hut_2.hut_damage(values)
                        elif(str == 'hut3'):
                            hut_3.hut_damage(values)
                        elif(str == 'hut4'):
                            hut_4.hut_damage(values)
                    if(str[0:6] == "cannon"):
                        number = int(str[-1])-1
                        values.cannon_health[number] = values.cannon_health[number] - \
                            values.queen_hit
                        cannon.cannon_damage(number, values)

                    if(str[0:7] == "wizzard"):
                        number = int(str[-1])-1
                        values.wizzard_health[number] = values.wizzard_health[number] - \
                            values.queen_hit
                        wizzard.wizzard_damage(number, values)

                    if(str == "wall"):
                        coi = wall_available.pop(0)
                        wall.wall_damage(
                            values, coi[0], coi[1])

    def queen_up(self, values, cannon):
        if(values.queen_alive == 1):
            values.frame[values.queen_x][values.queen_y] = " "
            x = values.queen_x
            l = [values.queen_y, values.queen_x-1*values.queen_step]
            if l in values.available:
                values.queen_x = values.queen_x - 1*values.queen_step
            else:
                values.queen_x = values.queen_x - 1
            l = [values.queen_y, x-1]
            if l in values.available:
                s = 1
            else:
                values.queen_x = x
            values.frame[values.queen_x][values.queen_y] = f"{Fore.GREEN}{Style.BRIGHT}Q{Style.RESET_ALL}"
            values.queen_prev = 'w'

    def queen_down(self, values, cannon):
        if(values.queen_alive == 1):
            values.frame[values.queen_x][values.queen_y] = " "
            x = values.queen_x
            l = [values.queen_y, values.queen_x+1*values.queen_step]
            if l in values.available:
                values.queen_x = values.queen_x + 1*values.queen_step
            else:
                values.queen_x = values.queen_x + 1
            l = [values.queen_y, x+1]
            if l in values.available:
                s = 1
            else:
                values.queen_x = x
            values.frame[values.queen_x][values.queen_y] = f"{Fore.GREEN}{Style.BRIGHT}Q{Style.RESET_ALL}"
            values.queen_prev = 's'

    def queen_left(self, values, cannon):
        if(values.queen_alive == 1):
            values.frame[values.queen_x][values.queen_y] = " "
            l = [values.queen_y-1*values.queen_step, values.queen_x]
            y = values.queen_y
            if l in values.available:
                values.queen_y = values.queen_y - 1*values.queen_step
            else:
                values.queen_y = values.queen_y - 1
            l = [y-1, values.queen_x]

            if l in values.available:
                s = 1
            else:
                values.queen_y = y

            values.frame[values.queen_x][values.queen_y] = f"{Fore.GREEN}{Style.BRIGHT}Q{Style.RESET_ALL}"
            values.queen_prev = 'a'

    def queen_right(self, values, cannon):
        if(values.queen_alive == 1):
            values.frame[values.queen_x][values.queen_y] = " "
            l = [values.queen_y+1*values.queen_step, values.queen_x]
            y = values.queen_y
            if l in values.available:
                values.queen_y = values.queen_y + 1*values.queen_step
            else:
                values.queen_y = values.queen_y + 1
            l = [y+1, values.queen_x]

            if l in values.available:
                s = 1
            else:
                values.queen_y = y
            values.frame[values.queen_x][values.queen_y] = f"{Fore.GREEN}{Style.BRIGHT}Q{Style.RESET_ALL}"
            values.queen_prev = 'd'
