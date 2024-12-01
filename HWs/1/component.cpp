#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;
class Graph {
private:
    int vertices;
    int edges;
    vector<vector<int>> graph;

public:
    Graph(int Vertex, int Edge) {
        vertices = Vertex;
        edges = Edge;
        graph.resize(Vertex);
    }

    void addEdge(int Vertex, int ww) {
        graph[Vertex].push_back(ww);
        graph[ww].push_back(Vertex);
    }

    void BFS(int node, unordered_set<int>& visited) {
        queue<int> queue;
        queue.push(node);
        visited.insert(node);

        while (queue.empty()!=true) {
            int current_node = queue.front();
            queue.pop();

            for (int neighbor : graph[current_node]) {
                if (visited.count(neighbor) == 0) {
                    visited.insert(neighbor);
                    queue.push(neighbor);
                }
            }
        }
    }

    int numComponents() {
        unordered_set<int> visited;
        int num_components = 0;

        for (int node = 0; node < vertices; node++) {
            if (visited.count(node) == 0) {
                BFS(node, visited);
                num_components++;
            }
        }

        return num_components;
    }
};

int main() {
    int num_vertices, num_edges;
    cin >> num_vertices >> num_edges;

    Graph g1(num_vertices, num_edges);

    for (int e = 0; e < num_edges; e++) {
        int x, y;
        std::cin >> x >> y;

        if (x <= num_vertices && y <= num_vertices) {
            g1.addEdge(x - 1, y - 1);
        }
    }

    cout << g1.numComponents() <<endl;

    return 0;
}