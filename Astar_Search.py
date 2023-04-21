#A*

graph = [
    ['S','E',60,50],
    ['S','X',99,999999],
    ['S','Y',99,9999],
    ['E','A',50,70],
    ['E','L',99,99900909090],
    ['L','F',99,99909],
    ['A','R',45,65],
    ['R','C',80,110],
    ['C','H',90,0],
    ['F','H',99,99000000000009]
    ]

nodes = set()
for i in graph:
    nodes.add(i[0])
    nodes.add(i[1])

def astar(graph,cost,open,close,curnode):
    if curnode in open:
        open.remove(curnode)
    close.add(curnode)
    for i in graph:
        if i[0] == curnode and cost[i[0]]+i[2]+i[3] < cost[i[1]]:
            open.add(i[1])
            cost[i[1]] = cost[i[0]]+i[2]+i[3]
            path[i[1]] = path[i[0]] + ' ---> '+ i[1]
    cost[curnode] = 999999999
    small = min(cost, key = cost.get)
    if small not in close:
        astar(graph,cost,open,close,small)

open,close = set(),set()
path,cost = {},{}

for i in nodes:
    cost[i] = 999999999
    path[i] = ''

s = input('Enter the start node: ')
path[s] = s
cost[s] = 0
astar(graph,cost,open,close,s)
g = input('Enter the goal node: ')
print('Path with least cost: ',path[g])
