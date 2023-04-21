# minimax

import math

def minimax(curdepth,nodeindex,maxturn,scores,targetdepth):

    if curdepth == targetdepth:
        return scores[nodeindex]

    if (maxturn):
        return max(minimax(curdepth+1,nodeindex*2,False,scores,targetdepth),minimax(curdepth+1,nodeindex*2 + 1,False,scores,targetdepth))

    else:
        return min(minimax(curdepth+1,nodeindex*2,True,scores,targetdepth),minimax(curdepth+1,nodeindex*2 + 1,True,scores,targetdepth))

scores = [-1,4,2,6,-3,-5,0,7]

treedepth = math.log(len(scores),2)
print('Tree depth :',treedepth)

print('Optimal value is :',end = ' ')
print(minimax(0,0,True,scores,treedepth))
