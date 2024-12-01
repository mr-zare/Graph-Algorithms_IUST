#include <iostream>
#include <vector>
using namespace std;

const int maxSize = 100010;
vector<int> graph[maxSize];
int visited[maxSize] = {0};
int ans = 1, counter = 0, index = 0;

void dfs(int node) {
    visited[node] = 1;
    for (int neighbor : graph[node]) {
        if (visited[neighbor] == 0) {
            dfs(neighbor);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    int x, y;
    for (int i = 0; i < m; ++i) {
        cin >> x >> y;
        x--, y--;
        graph[x].push_back(y);
        graph[y].push_back(x);
        index = x;
    }

    dfs(index);
    for (int i = 0; i < n; ++i) {
        if (visited[i] == 0 && graph[i].size() != 0) {
            counter += 3;
        }
        if (graph[i].size() % 2 == 1) {
            counter += 1;
        }
    }

    cout << (counter > 2 ? "NO" : "YES") << endl;

    return 0;
}
