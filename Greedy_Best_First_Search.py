graph = {
    'A' : [('B',12),('C',4)],
    'B' : [('D',7),('E',3)],
    'C' : [('F',8),('G',2)],
    'D' : [],
    'E' : [('H',0)],
    'F' : [('H',0)],
    'G' : [('H',0)]
    }
q,v = [],[]
def gbfs(graph,n,g,q,v):
    if n not in v:
        print(n)
        v.append(n)
    q += [i for i in graph[n] if i[0][0] not in v]
    q.sort(key = lambda x:x[1])
    temp = q.pop(0)
    if temp[0] == g:
        print(temp[0])
    else:
        gbfs(graph,temp[0],g,q,v)

gbfs(graph,'A','H',q,v)
