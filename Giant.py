from Enemy import *


class Giant(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Giant',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Giant is looking you without making any noise')
