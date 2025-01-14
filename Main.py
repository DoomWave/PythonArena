from Enemy import *
from Draugr import *
from Giant import *


def battle(e: Enemy):
    e.talk()
    e.attack()


Draugr = Draugr(10, 1)
Giant = Giant(50, 10)

battle(Draugr)
battle(Giant)
