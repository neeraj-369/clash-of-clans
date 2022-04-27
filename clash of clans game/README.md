# CLASH OF CLANS
###  By POLAVARAPU NEERAJ - 2020101026

## Overview

This is a mini version of clash of clans game designed to train people for the real game. This is a terminal version of the game. Player will be using keyboard keys to control and play. 

There will be two types of soldiers, one is king and other kind is troops, archers, balloons. if all the troops and king/queen dies, then the game will end. and there will be 4 kinds of buildings, which are cannons,wizzard towers, huts, townhall. if all of this got destroyed then it is victory for the player. along with this there are walls, just for the protection for the buildings.

there are 3 levels, if u succeed in one level, u will promote to next one. 

also there is a replay feature through which u can, view all the games replay.

Concepts of object oriented programming is present in the code. libraries used are colorama


## GUIDE

Requirements are python3, colorama. to install colorama do "pip install colorama"

to start the game do  - "python3 game.py"
to start replay of any game do  - "python3 replay.py"

## GAME RULES

* There will be king and troops(3 spawning areas)
* king is controlled by user, troops are automated(moves to the nearest building) and can be spawned by user)
* there are 3 types of buildings cannons, huts, townhall
* cannons can attack king and troops. if all the troops and kins is destroyed, then it is DEFEAT
* if all the buildings are destroyed it is VICTORY
* rage spell increases the movement speed and hit_power for troops alive and king
* heal spel increases the health of troops and king to 150%
* replay feature will just replay what every game we selected.
* there will be 3 levels, if u succed in any u will get promoted to next level. or if u fail the game ends. 
* u will get an option at begining to select between queen and king.
* queen can do AOE and also bonus attack has a delay of 1sec shoot.
* ballons can fly over any building and first targets cannons, wizzard towers. later attacks huts, townhall
* archers has range of attack, they can throw arrows at some location within range. 

## FUNCTIONALITIES :-
------------------

# controls
press `SPACE BAR` for king to attack
press `w` or `W` for king to move up
press `a` or `A` for king to move left
press `s` or `S` for king to move down
press `d` or `D` for king to move right
press `f` or `F` for troop to spawn at one location
press `g` or `G` for troop to spawn at one location
press `h` or `H` for troop to spawn at one location
press `j` or `J` for archer to spawn at one location
press `k` or `K` for archer to spawn at one location
press `l` or `L` for archer to spawn at one location
press `t` or `T` for balloon to spawn at one location
press `y` or `Y` for balloon to spawn at one location
press `u` or `U` for balloon to spawn at one location
press `b` or `B` for queens bonus attack with 1 sec delay shoot
press `e` or `E` for heal spell to activate
press `r` or `R` for rage spell to activate

- to start replay run `python3 replay.py` in terminal


# features
* Cannons will blink everytime a soldier comes near it
* color of buildings and troops change according to their health
* health bar at the top of frame in status bar along with time from start
* 3 types of buildings cannons, huts, town_hall
* replay feature for every game played
* wizzard towers will hit same as cannons along with it has area of attack of 3x3 AOE
* queen can attack at a range and along with it has an AOE
* for bonus task queen, can hit the target with AOE after 1 sec. 
* there are 3 levels, in first level there are 2 wizzard towers and 2 cannons and next level has 3 of them, and next has 4. 


# Description of classes created

* cannon class
in this class cannons get initiated, cannons will hit and damage to cannons will happen

* content class
content class is actually responsible for content in the game display, basically everything. i.e statusbar + frame

* handler class
this class is responsible for handling the user input requests and redirect to the respective class/method

* huts class
in this class huts are get initiated, huts get damaged and changes color

* input class
this is actually an important class, becuase this not only takes input, but it is input timer. which takes input with in given time period. or else goes to next step

* king class
in this class king got initiated and the moves are managed here

* spells class
in this class spells are declared both rage spell and heal spell and the backto normal after rage spell

* status class
displayed a status bar at the top of display with king health bar and time in seconds

* townhall class
in this class twonnhall gets initiated and damage to it is dealt here, also color change

* troop class
here troops are spawned in different locations and automated their location here.

* walls class
here all the walls are created

* replay class
here replay gets initiated for the specific history

* archer class
here archers are spawned in different locations and automated their location here.

* balloon class
here balloons are spawned in different locations and automated their location here.

* queen class
in this class queen got initiated and the moves are managed here

* wizzard class
in this class wizzards get initiated, cannons will hit and damage to cannons will happen


# OOP'S concept

* Inheritance
In this concept we can inhert(obtain) methods and properties of one parent class to many other child classes
In our code, the parent class is hut_structure. and child classes are hut_1, hut_2, hut_3...

```python
class hut_1(hut_structure):
    def __init__(self, values):
        value = 1
        self.x = values.hut[value-1][0]
        self.y = values.hut[value-1][1]
        super(hut_1, self).__init__(values, self.x, self.y, value)
    ...
```
* Polymorphism
In this concept we can define and change same methods in child present in parent class
in our code we have changed the init of hut_structure in its child classes, using SUPER command 

* Encapsulation
This concept is just the usage of classes and methods, which is used in entirely of our codes

* Abstraction
Abstraction is just, hiding the complexity and showing the code in easier way. eg is video player, in which we will be given buttons to play, stop. By hiding all the features(code).
examples in our code are king.moveup(), king.movedown(), king.hit(), hut.hut_damage(), troop_attack(), troop_automate(), troop_spawn(), cannon_fire(), cannon_damage(), etc....

