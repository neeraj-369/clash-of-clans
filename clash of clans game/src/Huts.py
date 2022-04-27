from colorama import Fore, Back, Style


class hut_structure:
    def __init__(self, values, x, y, value):
        self.x = x
        self.y = y
        for i in (self.x, self.x+1):
            for j in (self.y, self.y+1):
                a = i - self.x
                b = j - self.y
                if(a == 0 and b == 0):
                    values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}/{Style.RESET_ALL}"
                elif(a == 0 and b == 1):
                    values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT}\{Style.RESET_ALL}"
                else:
                    values.frame[i][j] = f"{Back.GREEN}{Style.BRIGHT} {Style.RESET_ALL}"
                l = [j, i]
                values.available.remove(l)
                values.object_near[i][j] = 'hut{}'.format(value)

    def hut_damage(self, values, x, y, value):

        if(values.huts_health[value] >= 20 and values.huts_health[value] < 50):
            for i in (x, x+1):
                for j in (y, y+1):
                    a = i - x
                    b = j - y
                    if(a == 0 and b == 0):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}/{Style.RESET_ALL}"
                    elif(a == 0 and b == 1):
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT}\{Style.RESET_ALL}"
                    else:
                        values.frame[i][j] = f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"

        elif(values.huts_health[value] > 0 and values.huts_health[value] < 20):
            for i in (x, x+1):
                for j in (y, y+1):
                    a = i - x
                    b = j - y
                    if(a == 0 and b == 0):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}/{Style.RESET_ALL}"
                    elif(a == 0 and b == 1):
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT}\{Style.RESET_ALL}"
                    else:
                        values.frame[i][j] = f"{Back.RED}{Style.BRIGHT} {Style.RESET_ALL}"

        elif(values.huts_health[value] <= 0):
            for i in (x, x+1):
                for j in (y, y+1):
                    values.frame[i][j] = " "
                    l = [j, i]
                    values.available.append(l)
            values.hut_alive[value] = 0


class hut_1(hut_structure):
    def __init__(self, values):
        value = 1
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_1, self).__init__(values, self.x, self.y, value)

    def hut_damage(self, values):
        value = 1
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_1, self).hut_damage(values, self.x, self.y, value-1)


class hut_2(hut_structure):
    def __init__(self, values):
        value = 2
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_2, self).__init__(values, self.x, self.y, value)

    def hut_damage(self, values):
        value = 2
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_2, self).hut_damage(values, self.x, self.y, value-1)


class hut_3(hut_structure):
    def __init__(self, values):
        value = 3
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_3, self).__init__(values, self.x, self.y, value)

    def hut_damage(self, values):
        value = 3
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_3, self).hut_damage(values, self.x, self.y, value-1)


class hut_4(hut_structure):
    def __init__(self, values):
        value = 4
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_4, self).__init__(values, self.x, self.y, value)

    def hut_damage(self, values):
        value = 4
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_4, self).hut_damage(values, self.x, self.y, value-1)
