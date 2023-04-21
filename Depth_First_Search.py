#dfs

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
n = 'A'
g = input('Goal node :')

temp = 0

def dfs(graph,n,v):
    global temp
    v.append(n)
    print(n)
    if n == g:
        print("Goal found")
        quit()

    else:
        for i in graph[n]:
            temp = 1
            dfs(graph,i,v)
    
    return temp

dfs(graph,n,v)

if temp == 1:
    print('Goal not found')
