import os
import json
from replays.show import show
show = show()

os.system('tput reset')
with open('./replays/history.txt', 'a') as k:
    song = 1
with open('./replays/history.txt', 'r') as f:
    try:
        s = json.load(f)
    except:
        print("NO GAME PLAYED YET")
        exit()

total_played = len(s)
game = 0

print("\n\nTOTAL GAMES PLAYED: {}".format(total_played), end=" ")
print("\t\t\t\tLATEST PLAYED GAME: {}".format(total_played))
print("\nSELECt GAME FOR REPLAY:", end=" ")

game = int(input())
if(game <= 0 or game > total_played):
    print("WRONG INPUT")
else:
    show.show(s[game-1])
