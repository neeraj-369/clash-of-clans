from colorama import Fore, Back, Style


class townhall:
    def __init__(self, values):
        for i in values.townhall_y:
            for j in values.townhall_x:
                a = i - values.townhall_y[0]
                b = j - values.townhall_x[0]
                if(values.townhall_health >= 50):
                    if((a == 0 and b == 1) or (a == 1 and b == 0)):
                        values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}/{Style.RESET_ALL}"
                    elif((a == 1 and b == 3) or (a == 0 and b == 2)):
                        values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}\{Style.RESET_ALL}"
                    elif((a == 2 and b == 0) or (a == 2 and b == 1) or (a == 2 and b == 2) or (a == 2 and b == 3)):
                        values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}-{Style.RESET_ALL}"
                    elif((a == 3 and b == 1) or (a == 3 and b == 2)):
                        values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}|{Style.RESET_ALL}"
                    elif((a == 1 and b == 1) or (a == 1 and b == 2)):
                        values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}o{Style.RESET_ALL}"
                    else:
                        values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT} {Style.RESET_ALL}"
                    l = [j, i]
                    values.available.remove(l)
                    values.object_near[i][j] = 'townhall'

    def townhall_damage(self, values):
        for i in values.townhall_y:

            for j in values.townhall_x:
                a = i - values.townhall_y[0]
                b = j - values.townhall_x[0]
                if(values.townhall_health >= 20 and values.townhall_health < 50):
                    if((a == 0 and b == 1) or (a == 1 and b == 0)):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}/{Style.RESET_ALL}"
                    elif((a == 1 and b == 3) or (a == 0 and b == 2)):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}\{Style.RESET_ALL}"
                    elif((a == 2 and b == 0) or (a == 2 and b == 1) or (a == 2 and b == 2) or (a == 2 and b == 3)):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}-{Style.RESET_ALL}"
                    elif((a == 3 and b == 1) or (a == 3 and b == 2)):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}|{Style.RESET_ALL}"
                    elif((a == 1 and b == 1) or (a == 1 and b == 2)):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}o{Style.RESET_ALL}"
                    else:
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"

                elif(values.townhall_health > 0 and values.townhall_health < 20):
                    if((a == 0 and b == 1) or (a == 1 and b == 0)):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}/{Style.RESET_ALL}"
                    elif((a == 1 and b == 3) or (a == 0 and b == 2)):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}\{Style.RESET_ALL}"
                    elif((a == 2 and b == 0) or (a == 2 and b == 1) or (a == 2 and b == 2) or (a == 2 and b == 3)):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}-{Style.RESET_ALL}"
                    elif((a == 3 and b == 1) or (a == 3 and b == 2)):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}|{Style.RESET_ALL}"
                    elif((a == 1 and b == 1) or (a == 1 and b == 2)):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}o{Style.RESET_ALL}"
                    else:
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT} {Style.RESET_ALL}"

                elif(values.townhall_health <= 0):
                    values.frame[i][j] = " "
                    l = [j, i]
                    values.available.append(l)
                    values.townhall_alive = 0
