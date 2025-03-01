def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
           dfs(graph, neighbor, visited)
 # 示例图
graph = {
 'A': ['B', 'C'],
 'B': ['A', 'D', 'E'],
 'C': ['A', 'F'],
 'D': ['B'],
 'E': ['B', 'F'],
 'F': ['C', 'E']
 }
 # 深度优先搜索
dfs(graph, 'A')  # 输出：A B D E F C
