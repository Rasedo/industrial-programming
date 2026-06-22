import math, sys
from datetime import datetime
def Calc_Func( x,y, op ):
    if op=='add':return x+y
    elif op=='sub':
        return x-y
    elif op=='mul':
        return x*y
    elif op=='div':
        if y==0: return None
        return x/y
    else: return 0
print( Calc_Func(10,5, 'add'))
