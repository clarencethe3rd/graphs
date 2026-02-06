graph = {
    "D": ["A","B"],
    "A": ["D","B"],
    "C": ["B"],
    "B": ["A","D","C"]
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

bfs(graph,"D")
                