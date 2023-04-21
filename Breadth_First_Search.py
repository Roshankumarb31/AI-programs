#bfs

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : [],
    'D' : [],
    'E' : ['F','G'],
    'F' : [],
    'G' : []
    }

v = []
o = []
s = 'A'
g = input('Goal node :')

o.append(s)

while o:
    temp = o.pop(0)
    v.append(temp)
    if temp == g:
        print('goal found')
        break

    else:
        for i in graph[temp]:
            o.append(i)

else:
    print('Goal not found')

print('open :',o)
print('visited :',v)
