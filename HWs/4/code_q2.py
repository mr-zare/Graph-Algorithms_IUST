from collections import defaultdict

max_nodes = 200010
adj_list = defaultdict(list)
visited = [0] * max_nodes
distances = [[0] * max_nodes for _ in range(3)]
leftmost_node, rightmost_node = 0, 0

def depth_first_search(node, mod):
    global distances, visited, adj_list
    visited[node] = 1
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            distances[mod][neighbor] = distances[mod][node] + 1
            depth_first_search(neighbor, mod)

def clear_distances(mod):
    global visited, distances
    visited = [0] * max_nodes
    distances[mod] = [0] * max_nodes

num_nodes = int(input())
for _ in range(num_nodes - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    adj_list[x].append(y)
    adj_list[y].append(x)

depth_first_search(0, 0)
rightmost_node = max(range(max_nodes), key=lambda x: distances[0][x])
clear_distances(0)
depth_first_search(rightmost_node, 0)
leftmost_node = max(range(max_nodes), key=lambda x: distances[0][x])

clear_distances(1)
depth_first_search(rightmost_node, 1)
clear_distances(2)
depth_first_search(leftmost_node, 2)

minimum_distance = max(distances[1][0], distances[2][0])
optimal_node = 0
for i in range(num_nodes):
    if max(distances[1][i], distances[2][i]) <= minimum_distance:
        optimal_node = i
        minimum_distance = max(distances[1][i], distances[2][i])
print(optimal_node + 1)
