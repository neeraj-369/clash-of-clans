from colorama import Fore, Back, Style


class king:
    def king_hit(self, values, townhall, hut_1, hut_2, hut_3, hut_4, wall, cannon, wizzard):

        if(values.king_alive == 1):
            if values.object_near[values.king_x-1][values.king_y] == "townhall":
                values.townhall_health = values.townhall_health-values.king_hit
                townhall.townhall_damage(values)

            if values.object_near[values.king_x-1][values.king_y] == "wall" or values.object_near[values.king_x+1][values.king_y] == "wall" or values.object_near[values.king_x][values.king_y-1] == "wall" or values.object_near[values.king_x][values.king_y+1] == "wall":
                if(values.object_near[values.king_x-1][values.king_y] != ' ' and values.object_near[values.king_x-1][values.king_y] == "wall"):
                    wall.wall_damage(values, values.king_x-1, values.king_y)

            if values.object_near[values.king_x-1][values.king_y][0:3] == "hut":
                if(values.object_near[values.king_x-1][values.king_y] != ' ' and values.object_near[values.king_x-1][values.king_y][0:3] == "hut"):
                    value = values.object_near[values.king_x-1][values.king_y]
                    number = int(value[-1])-1
                    values.huts_health[number] = values.huts_health[number] - \
                        values.king_hit

                    if(value == 'hut1'):
                        hut_1.hut_damage(values)
                    elif(value == 'hut2'):
                        hut_2.hut_damage(values)
                    elif(value == 'hut3'):
                        hut_3.hut_damage(values)
                    elif(value == 'hut4'):
                        hut_4.hut_damage(values)

            if values.object_near[values.king_x-1][values.king_y][0:6] == "cannon":
                if(values.object_near[values.king_x-1][values.king_y] != ' ' and values.object_near[values.king_x-1][values.king_y][0:6] == "cannon"):
                    value = values.object_near[values.king_x-1][values.king_y]
                    number = int(value[-1])-1
                    values.cannon_health[number] = values.cannon_health[number] - \
                        values.king_hit

                    cannon.cannon_damage(number, values)


            if values.object_near[values.king_x-1][values.king_y][0:7] == "wizzard":
                if(values.object_near[values.king_x-1][values.king_y] != ' ' and values.object_near[values.king_x-1][values.king_y][0:7] == "wizzard"):
                    value = values.object_near[values.king_x-1][values.king_y]
                    number = int(value[-1])-1
                    values.wizzard_health[number] = values.wizzard_health[number] - \
                        values.king_hit

                    wizzard.wizzard_damage(number, values)


    def king_up(self, values, cannon):
        if(values.king_alive == 1):
            values.frame[values.king_x][values.king_y] = " "
            x = values.king_x
            l = [values.king_y, values.king_x-1*values.king_step]
            if l in values.available:
                values.king_x = values.king_x - 1*values.king_step
            else:
                values.king_x = values.king_x - 1
            l = [values.king_y, x-1]
            if l in values.available:
                s = 1
            else:
                values.king_x = x
            values.frame[values.king_x][values.king_y] = f"{Fore.GREEN}{Style.BRIGHT}♔{Style.RESET_ALL}"

    def king_down(self, values, cannon):
        if(values.king_alive == 1):
            values.frame[values.king_x][values.king_y] = " "
            x = values.king_x
            l = [values.king_y, values.king_x+1*values.king_step]
            if l in values.available:
                values.king_x = values.king_x + 1*values.king_step
            else:
                values.king_x = values.king_x + 1
            l = [values.king_y, x+1]
            if l in values.available:
                s = 1
            else:
                values.king_x = x

            values.frame[values.king_x][values.king_y] = f"{Fore.GREEN}{Style.BRIGHT}♔{Style.RESET_ALL}"

    def king_left(self, values, cannon):
        if(values.king_alive == 1):
            values.frame[values.king_x][values.king_y] = " "
            l = [values.king_y-1*values.king_step, values.king_x]
            y = values.king_y
            if l in values.available:
                values.king_y = values.king_y - 1*values.king_step
            else:
                values.king_y = values.king_y - 1
            l = [y-1, values.king_x]

            if l in values.available:
                s = 1
            else:
                values.king_y = y

            values.frame[values.king_x][values.king_y] = f"{Fore.GREEN}{Style.BRIGHT}♔{Style.RESET_ALL}"

    def king_right(self, values, cannon):
        if(values.king_alive == 1):
            values.frame[values.king_x][values.king_y] = " "
            l = [values.king_y+1*values.king_step, values.king_x]
            y = values.king_y
            if l in values.available:
                values.king_y = values.king_y + 1*values.king_step
            else:
                values.king_y = values.king_y + 1
            l = [y+1, values.king_x]

            if l in values.available:
                s = 1
            else:
                values.king_y = y
            values.frame[values.king_x][values.king_y] = f"{Fore.GREEN}{Style.BRIGHT}♔{Style.RESET_ALL}"
