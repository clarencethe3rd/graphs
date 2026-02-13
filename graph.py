graph = {
    "D": ["B"],
    "A": ["C","B"],
    "C": ["A","E"],
    "B": ["A","D","E"],
    "E": ["B","C"]
}
#breadth-first search(BFS)
def bfs(graph,source):
    visited = set()
    queue = [source]
    while queue: 
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            for i in graph[node]:
                queue.append(i)

bfs(graph,"A")
def dfs(graph,source):
    visited = set()
    queue = [source]
    while queue:
        node = queue.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            for i in reversed(graph.get(node,[])):
                queue.append(i)
                
                
dfs(graph,"A")
