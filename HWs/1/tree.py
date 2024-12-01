import sys
sys.setrecursionlimit(10**6)

maxn = 2001
edge = [[0] * maxn for _ in range(maxn)]
mark = [0] * maxn
par = [0] * maxn
v = [[] for _ in range(maxn)]

def dfs(n):
    mark[n] = 1
    for i in v[n]:
        if not mark[i]:
            par[i] = n
            dfs(i)
        elif par[n] != i and not edge[i][n]:
            edge[n][i] = 1

def main():
    try:
        n, m = map(int, input().split())
        counter = -1
        for _ in range(m):
            x, y = map(int, input().split())
            x, y = x-1, y-1
            v[x].append(y)
            v[y].append(x)

        for i in range(n):
            if not mark[i]:
                counter += 1
                par[i] = i
                if counter:
                    edge[i][i - 1] = 2
                dfs(i)

        print(m - (n - 1 - counter), counter)
        for k in range(1, 3):
            for i in range(maxn):
                for j in range(maxn):
                    if edge[i][j] == k:
                        print(j + 1, i + 1)
    except ValueError:
        print("Invalid input format. Please provide valid integers.")

if __name__ == "__main__":
    main()