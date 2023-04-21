# alpha beta

import math
MAX = -math.inf
MIN = math.inf

def minimax(depth,nodeindex,maxturn,value,alpha,beta):

    if depth == 3:
        return value[nodeindex]

    if (maxturn):
        best = MAX
        for i in range(2):
            val = minimax(depth+1,nodeindex*2+i,False,value,alpha,beta)
            best = max(best,val)
            alpha = max(best,alpha)
            if alpha>=beta:
                break
        return best
    else:
        best = MIN
        for i in range(2):
            val = minimax(depth+1,nodeindex*2+i,True,value,alpha,beta)
            best = min(best,val)
            beta = min(best,alpha)
            if alpha>=beta:
                break
        return best
value = [-1,4,2,6,-3,-5,0,7]

print('Optimal value is :',end = ' ')
print(minimax(0,0,True,value,MAX,MIN))
