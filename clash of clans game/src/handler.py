from time import time
from src.king import king
from src.queen import queen
import os
import json


class input_handler:
    def input(self, symbol, values, king, townhall, hut_1, hut_2, hut_3, hut_4, wall, cannon, troop, spell, state, archer, balloon, queen, wizzard):
        if(symbol != ""):
            timei = time() - values.start_time
            dict = {"time": timei, "symbol": symbol}
            values.replaydata.append(dict)
            if(symbol == 'q' or symbol == 'Q'):
                os.system('tput reset')
                if(state == 'g'):
                    if(values.leveli == 0):
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
                exit()
        if(values.korq == 'k'):
            if(symbol == ' '):
                king.king_hit(values, townhall, hut_1, hut_2,
                              hut_3, hut_4, wall, cannon, wizzard)
            if(symbol == 'w' or symbol == 'W'):
                king.king_up(values, cannon)
            if(symbol == 's' or symbol == 'S'):
                king.king_down(values, cannon)
            if(symbol == 'a' or symbol == 'A'):
                king.king_left(values, cannon)
            if(symbol == 'd' or symbol == 'D'):
                king.king_right(values, cannon)

        if(values.korq == 'q'):
            if(symbol == ' '):
                values.queen_range = 8
                values.queen_side = 5
                queen.queen_hit(values, townhall, hut_1, hut_2,
                                hut_3, hut_4, wall, cannon, wizzard)
            if(symbol == 'b'):
                values.q_b = 1
                values.queen_range = 16
                values.queen_side = 9
                values.q_time = time()
                # queen.queen_hit(values, townhall, hut_1, hut_2,
                #                 hut_3, hut_4, wall, cannon, wizzard)
            if(symbol == 'w' or symbol == 'W'):
                queen.queen_up(values, cannon)
            if(symbol == 's' or symbol == 'S'):
                queen.queen_down(values, cannon)
            if(symbol == 'a' or symbol == 'A'):
                queen.queen_left(values, cannon)
            if(symbol == 'd' or symbol == 'D'):
                queen.queen_right(values, cannon)

        if(symbol == 'f' or symbol == 'F'):
            troop.spawn(values, symbol)
        if(symbol == 'g' or symbol == 'G'):
            troop.spawn(values, symbol)
        if(symbol == 'h' or symbol == 'H'):
            troop.spawn(values, symbol)
        if(symbol == 'j' or symbol == 'J'):
            archer.spawn(values, symbol)
        if(symbol == 'k' or symbol == 'K'):
            archer.spawn(values, symbol)
        if(symbol == 'l' or symbol == 'L'):
            archer.spawn(values, symbol)
        if(symbol == 't' or symbol == 'T'):
            balloon.spawn(values, symbol)
        if(symbol == 'y' or symbol == 'Y'):
            balloon.spawn(values, symbol)
        if(symbol == 'u' or symbol == 'U'):
            balloon.spawn(values, symbol)
        if(symbol == 'e' or symbol == 'E'):
            spell.healspell(values)
        if(symbol == 'r' or symbol == 'R'):
            if(values.rage_active == 0):
                spell.ragespell(values)
