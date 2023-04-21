#ucs

graph = {
    'S' : [('A',2),('B',3),('D',5)],
    'A' : [('C',4)],
    'B' : [('D',5)],
    'C' : [('G',2)],
    'D' : [('G',5)],
    'G' : []
    }

def pc(path):
    tc = 0
    for n,c in path:
        tc += c
    return tc

def ucs(graph,s,g):
    v = []
    q = [[(s,0)]]
    while q:
        q.sort(key = pc)
        path = q.pop(0)
        n = path[-1][0]
        if n in v:
            continue
        v.append(n)
        if n == g:
            return path
        else:
            an = graph.get(n,[])
            for newn,c in an:
                newp = path.copy()
                newp.append((newn,c))
                q.append(newp)

sol = ucs(graph,'S','G')
print('Path :',sol)
print('Cost :',pc(sol))
