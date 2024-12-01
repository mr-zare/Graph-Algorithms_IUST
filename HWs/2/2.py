import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

mark = [False] * (10**6 + 10)
is_point = [False] * (10**6 + 10)
dp = [0] * (10**6 + 10)
h = [0] * (10**6 + 10)
adj = defaultdict(list)
edge = []
mp = defaultdict(dict)
counter_edge = 0
ans = 0

def dfs(v, parent, index):
    global ans
    dp[v] = h[v]
    mark[v] = True
    for i in range(len(adj[v])):
        u, ind = adj[v][i]
        if not mark[u]:
            h[u] = h[v] + 1
            dfs(u, v, ind)
            dp[v] = min(dp[v], dp[u])
        elif u != parent:
            dp[v] = min(dp[v], h[u])
    if v != 1 and dp[v] == h[v]:
        is_point[index] = True
    return

n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    if u > v:
        u, v = v, u
    if u != v:
        if not mp[u].get(v):
            adj[u].append((v, counter_edge))
            adj[v].append((u, counter_edge))
            edge.append((u, v))
            counter_edge += 1
        mp[u][v] = mp[u].get(v, 0) + 1

dfs(1, 0, 0)
for i in range(counter_edge):
    if is_point[i] and mp[edge[i][0]].get(edge[i][1]) == 1:
        ans += 1

print(ans)
