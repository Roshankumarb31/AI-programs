# idastar

graph = {
    'A' : ['B','C'],
    'B' : ['D','E','F'],
    'C' : ['G','H','I','J'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : []
    }

f_score = {'A':8,'B':11,'C':6,'D':23,'E':24,'F':18,'G':13,'H':7,'I':8,'J':14}

start = 'A'
goal = input('Enter the goal node :')
greater_fscore,visited = [],[]
f = f_score[start]

def idastar(graph,f_score,start,f):
    global greater_fscore,visited
    for i in graph[start]:
        if f_score[i] > f:
            greater_fscore.append(f_score[i])
        elif f_score[goal] > f:
            f = f_score[goal]
            greater_fscore, visited = [],[]
            idastar(graph,f_score,start,f)
        else:
            visited.append(i)
            if i == goal:
                print('Goal found ',goal)
                print('Visited ',visited)
                print('Greater F values ',greater_fscore)
                break
            else:
                idastar(graph,f_score,i,f)
idastar(graph,f_score,start,f)
