

class walls:
    def __init__(self, values):

        for i in range(8, 42):
            values.frame[i][24] = values.wall_symbol
            values.frame[i][111] = values.wall_symbol
            l = [111, i]
            values.available.remove(l)
            l = [24, i]
            values.available.remove(l)
            values.object_near[i][24] = 'wall'
            values.object_near[i][111] = 'wall'

        for j in range(25, 111):
            values.frame[8][j] = values.wall_symbol
            values.frame[41][j] = values.wall_symbol
            l = [j, 8]
            values.available.remove(l)
            l = [j, 41]
            values.available.remove(l)
            values.object_near[8][j] = 'wall'
            values.object_near[41][j] = 'wall'

        for i in range(23, 29):
            values.frame[i][64] = values.wall_symbol
            values.frame[i][75] = values.wall_symbol
            l = [64, i]
            values.available.remove(l)
            l = [75, i]
            values.available.remove(l)
            values.object_near[i][64] = 'wall'
            values.object_near[i][75] = 'wall'

        for j in range(65, 75):
            values.frame[28][j] = values.wall_symbol
            values.frame[21][j] = values.wall_symbol
            l = [j, 28]
            values.available.remove(l)
            l = [j, 21]
            values.available.remove(l)
            values.object_near[28][j] = 'wall'
            values.object_near[21][j] = 'wall'

    def wall_damage(self, values, x, y):
        values.frame[x][y] = ' '
        l = [y, x]
        values.available.append(l)
