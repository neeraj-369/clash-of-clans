from time import time
from colorama import Fore, Back, Style


class values:
    # 🤴
    def __init__(self):
        self.counter = 0
        self.start_time = time()
        self.timestep = 0.2
        self.percentage_boxlength = 30
        self.fill = '█'
        self.percentage = 100
        self.frame_length = 140
        self.frame_height = 50
        self.townhall_health = 100
        self.hut_health = 100
        self.king_hit = 10
        self.queen_hit = 9
        self.available = []
        self.frame = [[" " for i in range(self.frame_length)]
                      for j in range(self.frame_height)]
        self.king_x = self.frame_height-2
        self.king_y = int((self.frame_length-2)/2)
        self.queen_x = self.frame_height-2
        self.queen_y = int((self.frame_length-2)/2)
        for i in range(1, self.frame_length-1):
            self.frame[0][i] = f"{Fore.MAGENTA}{Style.BRIGHT}-{Style.RESET_ALL}"
            self.frame[self.frame_height -
                       1][i] = f"{Fore.MAGENTA}{Style.BRIGHT}-{Style.RESET_ALL}"
        for j in range(1, self.frame_height-1):
            self.frame[j][0] = f"{Fore.MAGENTA}{Style.BRIGHT}|{Style.RESET_ALL}"
            self.frame[j][self.frame_length -
                          1] = f"{Fore.MAGENTA}{Style.BRIGHT}|{Style.RESET_ALL}"
        for i in range(1, self.frame_length-1):
            for j in range(1, self.frame_height-1):
                l = [i, j]
                self.available.append(l)

        self.frame[self.king_x][self.king_y] = f"{Fore.GREEN}{Style.BRIGHT}♔{Style.RESET_ALL}"
        self.frame[self.queen_x][self.queen_y] = f"{Fore.GREEN}{Style.BRIGHT}Q{Style.RESET_ALL}"

        self.townhall_x = [68, 69, 70, 71]
        self.townhall_y = [23, 24, 25, 26]
        self.object_near = [[" " for i in range(0, self.frame_length)]
                            for j in range(0, self.frame_height)]
        self.numberofhuts = 4
        self.huts_health = []
        for i in range(0, self.numberofhuts):
            self.huts_health.append(100)
        self.wall_symbol = f"{Fore.CYAN}{Style.BRIGHT}▢{Style.RESET_ALL}"
        self.cannon_symbol = f"{Fore.BLUE}{Back.GREEN}{Style.BRIGHT}▣{Style.RESET_ALL}"
        self.wizzard_symbol = f"{Fore.BLUE}{Back.GREEN}{Style.BRIGHT}w{Style.RESET_ALL}"
        self.numberofcannons = 4
        self.numberofwizzards = 4
        self.cannons = []
        self.cannons.append([5, 120])
        self.cannons.append([45, 15])
        self.cannons.append([10, 68])
        self.cannons.append([45, 120])
        self.wizzards = []
        self.wizzards.append([5, 125])
        self.wizzards.append([45, 20])
        self.wizzards.append([15, 68])
        self.wizzards.append([40, 120])
        self.rangeofcannon = 6
        self.rangeofwizzard = 6
        self.cannon_hit = 5
        self.wizzard_hit = 5
        self.tic = []
        for i in range(0, self.numberofcannons):
            self.tic.append(0)
        self.tici = []
        for i in range(0, self.numberofwizzards):
            self.tici.append(0)
        self.cannon_timestep = 0.8
        self.wizzard_timestep = 0.8
        self.troop_symbol = f"{Fore.GREEN}{Style.BRIGHT}♖{Style.RESET_ALL}"
        self.archer_symbol = f"{Fore.GREEN}{Style.BRIGHT}a{Style.RESET_ALL}"
        self.balloon_symbol = f"{Fore.GREEN}{Style.BRIGHT}b{Style.RESET_ALL}"
        self.numberofspawns = 3
        self.troops = []
        self.archers = []
        self.balloons = []
        self.troop_hit = 8
        self.archer_hit = 4
        self.balloon_hit = 16
        self.hut = []
        self.hut.append([10, 30])
        self.hut.append([10, 34])
        self.hut.append([38, 30])
        self.hut.append([5, 115])
        self.troop = []
        self.troop.append(0)
        self.troop.append(0)
        self.troop.append(0)
        self.troop.append(0)
        self.troop.append(0)
        self.troop.append(0)

        self.archer = []
        self.archer.append(0)
        self.archer.append(0)
        self.archer.append(0)
        self.archer.append(0)
        self.archer.append(0)
        self.archer.append(0)
        self.balloon = []
        self.balloon.append(0)
        self.balloon.append(0)
        self.balloon.append(0)
        self.balloon.append(0)
        self.balloon.append(0)
        self.balloon.append(0)
        self.toc = 0
        self.toci = 0
        self.tocii = 0
        self.numberoftroops = 6
        self.numberofarchers = 6
        self.numberofballoons = 3
        self.troop_timestep = 0.5
        self.archer_timestep = 0.25
        self.balloon_timestep = 0.25
        self.cannon_health = []
        self.cannon_health.append(100)
        self.cannon_health.append(100)
        self.cannon_health.append(100)
        self.cannon_health.append(100)
        self.wizzard_health = []
        self.wizzard_health.append(100)
        self.wizzard_health.append(100)
        self.wizzard_health.append(100)
        self.wizzard_health.append(100)
        self.troop_health = []
        self.troop_health.append(100)
        self.troop_health.append(100)
        self.troop_health.append(100)
        self.troop_health.append(100)
        self.troop_health.append(100)
        self.troop_health.append(100)

        self.archer_health = []
        self.archer_health.append(50)
        self.archer_health.append(50)
        self.archer_health.append(50)
        self.archer_health.append(50)
        self.archer_health.append(50)
        self.archer_health.append(50)

        self.balloon_health = []
        self.balloon_health.append(100)
        self.balloon_health.append(100)
        self.balloon_health.append(100)
        self.balloon_health.append(100)
        self.balloon_health.append(100)
        self.balloon_health.append(100)

        self.king_alive = 1
        self.queen_alive = 1
        self.troop_alive = []
        self.troop_alive.append(0)
        self.troop_alive.append(0)
        self.troop_alive.append(0)
        self.troop_alive.append(0)
        self.troop_alive.append(0)
        self.troop_alive.append(0)

        self.archer_alive = []
        self.archer_alive.append(0)
        self.archer_alive.append(0)
        self.archer_alive.append(0)
        self.archer_alive.append(0)
        self.archer_alive.append(0)
        self.archer_alive.append(0)

        self.balloon_alive = []
        self.balloon_alive.append(0)
        self.balloon_alive.append(0)
        self.balloon_alive.append(0)
        self.balloon_alive.append(0)
        self.balloon_alive.append(0)
        self.balloon_alive.append(0)

        self.troop_done = []
        self.troop_done.append(0)
        self.troop_done.append(0)
        self.troop_done.append(0)
        self.troop_done.append(0)
        self.troop_done.append(0)
        self.troop_done.append(0)

        self.archer_done = []
        self.archer_done.append(0)
        self.archer_done.append(0)
        self.archer_done.append(0)
        self.archer_done.append(0)
        self.archer_done.append(0)
        self.archer_done.append(0)

        self.balloon_done = []
        self.balloon_done.append(0)
        self.balloon_done.append(0)
        self.balloon_done.append(0)
        self.balloon_done.append(0)
        self.balloon_done.append(0)
        self.balloon_done.append(0)

        self.hut_alive = []
        self.cannon_alive = []
        self.wizzard_alive = []
        self.townhall_alive = 1
        for i in range(0, self.numberofhuts):
            self.hut_alive.append(1)
        for i in range(0, self.numberofcannons):
            self.cannon_alive.append(1)
        for i in range(0, self.numberofwizzards):
            self.wizzard_alive.append(1)
        self.king_step = 1
        self.queen_step = 1
        self.rage_time = 3
        self.rage_active = 0
        self.tim = time()
        self.start_time = time()
        self.replaydata = []
        self.barbarian_count = 0
        self.archer_count = 0
        self.balloon_count = 0
        self.rangeofarcher = 5
        self.balloon_prev = []
        self.balloon_prev.append(" ")
        self.balloon_prev.append(" ")
        self.balloon_prev.append(" ")
        self.korq = 'k'
        self.queen_prev = 'w'
        self.queen_range = 8
        self.queen_side = 5
        self.q_b = 0
        self.q_time = 0
        self.leveli = 0
