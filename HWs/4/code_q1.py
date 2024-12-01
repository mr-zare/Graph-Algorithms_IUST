MAXN = 200010
v = [[] for _ in range(MAXN)]
mark = [0] * MAXN
high = [0] * MAXN

def dfs(n):
    global mark, high  # Declare global variables
    mark[n] = 1
    for i in v[n]:
        if not mark[i]:
            high[i] = high[n] + 1
            dfs(i)

def main():
    global mark, high  # Declare global variables
    n = int(input())
    for i in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        v[x].append(y)
        v[y].append(x)
    
    dfs(0)
    firstNode = max(range(MAXN), key=lambda i: high[i])
    mark = [0] * MAXN
    high = [0] * MAXN
    dfs(firstNode)
    print(max(high))

if __name__ == "__main__":
    main()
