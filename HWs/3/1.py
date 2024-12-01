from collections import defaultdict

def dfs(node, parent, graph, colors):
    color = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            if color == colors[node]:
                color += 1
            colors[neighbor] = color
            dfs(neighbor, node, graph, colors)
            color += 1

# Read input
n = int(input())
graph = defaultdict(list)

for _ in range(n - 1):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

colors = [0] * (n + 1)
colors[1] = 1  
dfs(1, 0, graph, colors)

max_color = max(colors)
if(n==1):
    max_color=0
print(max_color) 
