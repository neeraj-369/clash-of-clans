from time import time


class spell:
    def ragespell(self, values):
        values.tim = time()
        values.rage_active = 1
        if(values.korq == 'k'):
            values.king_hit = values.king_hit*2
        if(values.korq == 'q'):
            values.queen_hit = values.queen_hit*2
        values.troop_hit = values.troop_hit*2
        values.troop_timestep = values.troop_timestep/2

        values.archer_hit = values.archer_hit*2
        values.archer_timestep = values.archer_timestep/2

        values.balloon_hit = values.balloon_hit*2
        values.balloon_timestep = values.balloon_timestep/2

        if(values.korq == 'k'):
            values.king_step = int(values.king_step*2)
        if(values.korq == 'q'):
            values.queen_step = int(values.queen_step*2)

    def ragenormal(self, values):
        if(values.korq == 'k'):
            values.king_hit = values.king_hit/2
        if(values.korq == 'q'):
            values.queen_hit = values.queen_hit/2

        values.troop_hit = values.troop_hit/2
        values.troop_timestep = values.troop_timestep*2

        values.archer_hit = values.archer_hit/2
        values.archer_timestep = values.archer_timestep*2

        values.archer_hit = values.archer_hit/2
        values.archer_timestep = values.archer_timestep*2

        if(values.korq == 'k'):
            values.king_step = int(values.king_step/2)
        if(values.korq == 'q'):
            values.queen_step = int(values.queen_step/2)

    def healspell(self, values):
        values.percentage = values.percentage*1.5
        if(values.percentage >= 100):
            values.percentage = 100
        for i in range(0, values.barbarian_count):
            values.troop_health[i] = values.troop_health[i]*1.5
            if(values.troop_health[i] >= 100):
                values.troop_health[i] = 100

        for i in range(0, values.archer_count):
            values.archer_health[i] = values.archer_healtha[i]*1.5
            if(values.archer_health[i] >= 100):
                values.archer_health[i] = 100

        for i in range(0, values.balloon_count):
            values.balloon_health[i] = values.balloon_health[i]*1.5
            if(values.balloon_health[i] >= 100):
                values.balloon_health[i] = 100
