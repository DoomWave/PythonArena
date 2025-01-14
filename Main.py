from Enemy import *
from Draugr import *
from Giant import *

Draugr = Draugr(10, 1)
Giant = Giant(50, 10)

print(f'{Draugr.get_type_of_enemy()} has {Draugr.health_points} health points and can do attack of {Draugr.attack_damage}')
print(f'{Giant.get_type_of_enemy()} has {Giant.health_points} health points and can do attack of {Giant.attack_damage}')

Draugr.talk()
Giant.talk()
