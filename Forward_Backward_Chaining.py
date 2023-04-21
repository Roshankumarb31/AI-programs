import aima
from aima.utils import *
import aima.logic

clauses = [
    aima.utils.expr('American(x) & Weapon(y) & Hostile(z) & Sells(x,y,z) ==> Criminal(x)'),
    aima.utils.expr('Enemy(Nono,America)'),
    aima.utils.expr('Owns(Nono,M1)'),
    aima.utils.expr('Missile(M1)'),
    aima.utils.expr('Missile(x) & Owns(Nono,x) ==> Sells(West,x,Nono)'),
    aima.utils.expr('American(West)'),
    aima.utils.expr('Missile(x) ==> Weapon(x)')
           ]

#knowledge base
KB = aima.logic.FolKB(clauses)

#rules
KB.tell(aima.utils.expr('Enemy(Coco,America)'))
KB.tell(aima.utils.expr('Enemy(Jojo,America)'))
KB.tell(aima.utils.expr('Enemy(x,America) ==> Hostile(x)'))

#forward chaining
hostile = aima.logic.fol_fc_ask(KB,aima.utils.expr('Hostile(x)'))
criminal = aima.logic.fol_fc_ask(KB,aima.utils.expr('Criminal(x)'))

print('Forward Chaining')
print('Hostile?\n',list(hostile))
print('\nCriminal\n',list(criminal))

#backward chaining
hotile = KB.ask(aima.utils.expr('Hostile(x)'))
criminal = KB.ask(aima.utils.expr('Criminal(x)'))

print('Backward Chaining')
print('\nHostile?\n',list(hostile))
print('\nCriminal\n',list(criminal))
