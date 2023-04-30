g = [
    [1],
    [0, 2],
    [1],
    [],
    [5],
    [4]
]

vis = [False for i in range(6)]

def dfs(v):
    print(v)
    vis[v] = True
    for el in g[v]:
        if not vis[el]:
            dfs(el)

for i in range(6):
    if not vis[i]:
        dfs(i)
        print()
