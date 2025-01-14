from Enemy import *
import random


class Draugr(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Draugr',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('*Grumbling in Nordic Language*')

    def battle_cry(self):
        print('The Draugr is screaming his battle cry')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.70
        if did_special_attack_work:
            self.attack_damage += 5
            print('The Draugr is invoking his Thu-um')
