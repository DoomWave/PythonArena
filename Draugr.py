from Enemy import *


class Draugr(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Draugr',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('*Grumbling in Nordic Language*')

    def battle_cry(self):
        print('The Draugr is screaming his battle cry')
