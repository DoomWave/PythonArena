from Enemy import *
import random

class Giant(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Giant',
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Giant is looking you without making any noise')


    def special_attack(self):
        did_special_attack_work = random.random() < 0.30
        if did_special_attack_work:
            self.attack_damage += 25
            print('The Giant is using his big hammer to attack to blow away in the sky')
