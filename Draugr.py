from Enemy import *

class Draugr(Enemy):

    def __init__(self, type_of_enemy, health_points, attack_damage):
        super().__init__(type_of_enemy=type_of_enemy, health_points=health_points, attack_damage=attack_damage)
