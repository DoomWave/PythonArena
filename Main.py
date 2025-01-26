from Enemy import *
from Draugr import *
from Giant import *
from Hero import *
from Weapon import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points> 0 and e2.health_points > 0:
        print('--------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.attack_damage} Damage Points increased')
        print(f'{e2.get_type_of_enemy()}: {e2.attack_damage} Damage Points increased')
        e2.attack()
        e1.health_points  -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
        
    print('--------')

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')


def hero_battle(hero: Hero, enemy: Enemy):


    while hero.health_points> 0 and enemy.health_points > 0:
        print('--------')
        print(f'Hero: {hero.attack_damage} Damage Points increased')
        print(f'{enemy.get_type_of_enemy()}: {enemy.attack_damage} Damage Points increased')
        enemy.attack()
        hero.health_points  -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
        
    print('--------')

    enemy.special_attack()

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')

draugr = Draugr(10, 5)
giant = Giant(50, 10)
hero = Hero(12, 3)
weapon = Weapon('DragonSlayer', 55)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, giant)

