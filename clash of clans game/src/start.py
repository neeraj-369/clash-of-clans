from src.content import content as contenti
from src.input import input_timer as input_timeri
from src.handler import input_handler
from src.values import values as valuesi
from src.king import king as kingi
from src.queen import queen as queeni
from src.Townhall import townhall as townhalli
from src.Walls import walls
from src.Cannons import cannon as cannoni
from src.wizzard import wizzard as wizzardi
import src.Huts
from time import time, sleep
from src.troop import troop as troopi
from src.spells import spell as spelli
from src.archer import archer as archeri
from src.balloon import balloon as ballooni
import os
import json
from colorama import Fore, Back, Style


class start:
    korqi = 'k'
    # sample_list = []
    for level in range(0, 3):
        values = valuesi()

        values.leveli = level
        values.numberofcannons = level + 2
        values.numberofwizzards = level + 2

        if(level == 0):

            while(True):
                os.system('tput reset')
                values.korq = input(
                    '\n\nIF U WANT TO PLAY WITH KING PRESS K OR IF WITH QUEEN PRESS Q: ')
                if(values.korq == 'K'):
                    values.korq = 'k'
                if(values.korq == 'Q'):
                    values.korq = 'q'
                if(values.korq == 'k'):
                    values.frame[values.king_x][values.king_y] = f"{Fore.GREEN}{Style.BRIGHT}♔{Style.RESET_ALL}"
                if(values.korq == 'q' or values.korq == 'k'):
                    break

        if(level == 0):
            korqi = values.korq
        else:
            values.korq = korqi

        content = contenti()
        inputi = input_timeri()
        handler = input_handler()

        king = kingi()
        queen = queeni()
        townhall = townhalli(values)
        hut_1 = src.Huts.hut_1(values)
        hut_2 = src.Huts.hut_2(values)
        hut_3 = src.Huts.hut_3(values)
        hut_4 = src.Huts.hut_4(values)
        wall = walls(values)
        victory = [

            " ___        ___ _______  ________   __________    ______    _____     ___    ___  ",
            " \  \      /  / |_   _| |   _____| |___    ___|  /  __  \  |  ___ \   \  \  /  /  ",
            "  \  \    /  /    | |   |  |           |  |     |  /   \ | | |___) |   \  \/  /   ",
            "   \  \  /  /     | |   |  |           |  |     |  |   | | |  __  /     \    /    ",
            "    \  \/  /    __| |__ |  |_____      |  |     |   \_/  | | |  \ \      |  |     ",
            "     \____/    |_______||________|     |__|      \______/  |_|   \_\     |__|     ",
            "                                                                                  "

        ]
        defeat = [
            "  _____     _______     _______    _______         ___        __________       ",
            " |  __  \  |  _____|   |  _____|  |  _____|       /    \     |___    ___|         ",
            " | |  | |  | |_____    | |_____   | |_____       /  /\  \        |  |          ",
            " | |  | |  |  _____|   |  _____|  |  _____|     /  /__\  \       |  |         ",
            " | |__/ |  | |_____    | |        | |_____     /  /    \  \      |  |        ",
            " |______/  |_______|   |_|        |_______|   |___|     |__|     |__|          ",
            "                                                                                 "
        ]
        cannon = cannoni(values)
        wizzard = wizzardi(values)
        for i in range(values.numberofcannons):
            values.tic[i] = time()
        for i in range(values.numberofwizzards):
            values.tici[i] = time()
        troop = troopi()
        values.toc = time()
        spell = spelli()
        tim = time()
        archer = archeri()
        balloon = ballooni()

        while True:
            content.status(values)
            inputi.input_timer(values)
            handler.input(inputi.symbol, values, king,
                          townhall, hut_1, hut_2, hut_3, hut_4, wall, cannon, troop, spell, 'g', archer, balloon, queen, wizzard)
            cannon.cannon_hit(values)
            wizzard.wizzard_hit(values)

            if(values.q_b == 1):
                if(time() - values.q_time >= 1):
                    queen.queen_hit(values, townhall, hut_1,
                                    hut_2, hut_3, hut_4, wall, cannon, wizzard)
                    values.q_b = 0

            if(time() - values.toc >= values.troop_timestep):
                values.toc = time()
                for i in range(0, values.barbarian_count):
                    if(values.troop[i] == 1):
                        if(values.troop_alive[i] != 0):
                            troop.automate(i, values, hut_1, hut_2,
                                           hut_3, hut_4, townhall, cannon, wizzard)

            if(time() - values.toci >= values.archer_timestep):
                values.toci = time()
                for i in range(0, values.archer_count):
                    if(values.archer[i] == 1):
                        if(values.archer_alive[i] != 0):
                            archer.automate(i, values, hut_1, hut_2,
                                            hut_3, hut_4, townhall, cannon, wizzard)

            if(time() - values.tocii >= values.balloon_timestep):
                values.tocii = time()
                for i in range(0, values.balloon_count):
                    if(values.balloon[i] == 1):
                        if(values.balloon_alive[i] != 0):
                            balloon.automate(i, values, hut_1, hut_2,
                                             hut_3, hut_4, townhall, cannon, wizzard)

            if(values.rage_active == 1):
                if(time() - values.tim >= values.rage_time):
                    values.rage_active = 0
                    spell.ragenormal(values)

            count = 0
            for i in range(0, values.numberofhuts):
                count = count + values.hut_alive[i]

            for i in range(0, values.numberofcannons):
                count = count + values.cannon_alive[i]

            for i in range(0, values.numberofwizzards):
                count = count + values.wizzard_alive[i]

            count = count + values.townhall_alive
            if(count == 0):
                os.system('tput reset')
                if(level == 0):
                    with open('./replays/history.txt', 'a') as k:
                        song = 1
                    with open('./replays/history.txt', 'r') as f:
                        try:
                            s = json.load(f)
                        except:
                            s = []
                    k = []
                    x = {"korq": values.korq}
                    k.append(x)
                    k.append(values.replaydata)
                    s.append(k)

                    with open('./replays/history.txt', 'w') as g:
                        json.dump(s, g,
                                  ensure_ascii=False, indent=4)
                else:
                    with open('./replays/history.txt', 'a') as k:
                        song = 1
                    with open('./replays/history.txt', 'r') as f:
                        try:
                            s = json.load(f)
                        except:
                            s = []
                    s[len(s) - 1].append(values.replaydata)
                    with open('./replays/history.txt', 'w') as g:
                        json.dump(s, g,
                                  ensure_ascii=False, indent=4)

                for i in victory:
                    print(i)
                if(level == 2):
                    exit()
                else:
                    print('\n next level will start in 5sec')
                    sleep(5)
                    break

            counti = 0
            for i in range(0, values.barbarian_count):
                counti = counti + values.troop_alive[i]
            if(values.korq == 'k'):
                counti = counti + values.king_alive
            if(values.korq == 'q'):
                counti = counti + values.queen_alive

            if(counti == 0):
                os.system('tput reset')
                if(level == 0):
                    with open('./replays/history.txt', 'a') as k:
                        song = 1
                    with open('./replays/history.txt', 'r') as f:
                        try:
                            s = json.load(f)
                        except:
                            s = []
                    k = []
                    x = {"korq": values.korq}
                    k.append(x)
                    k.append(values.replaydata)
                    s.append(k)
                    with open('./replays/history.txt', 'w') as g:
                        json.dump(s, g,
                                  ensure_ascii=False, indent=4)
                else:
                    with open('./replays/history.txt', 'a') as k:
                        song = 1
                    with open('./replays/history.txt', 'r') as f:
                        try:
                            s = json.load(f)
                        except:
                            s = []
                    s[len(s) - 1].append(values.replaydata)
                    with open('./replays/history.txt', 'w') as g:
                        json.dump(s, g,
                                  ensure_ascii=False, indent=4)
                for i in defeat:
                    print(i)
                exit()
