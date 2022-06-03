from collections import deque


def bfs(graph):
    # граф должен быть связным
    queue = deque()
    queue.append(1)
    visited = set()
    dist_from_first = {i: float("inf") for i in range(1, len(graph) + 1)}

    while queue:
        v = queue.popleft()
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                queue.append(u)
                dist_from_first[u] = min(
                    dist_from_first[v] + 1, dist_from_first[u])
