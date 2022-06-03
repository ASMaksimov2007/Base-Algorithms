topsort_list = []


def topsort(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            topsort(u)

    topsort_list.append(v)


topsort_list.reverse()
