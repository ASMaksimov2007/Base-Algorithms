# Предопределение графа graph как списка смежности
visited = [False] * len(graph)


def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
