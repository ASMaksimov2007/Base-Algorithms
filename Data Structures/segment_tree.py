array = [1, 4, 1, 9, 2, 7, 8, 2, -1, 6]

segment_tree = [0] * (4 * len(array))


def build(l, r, cur_vertex):
    if l + 1 == r:
        segment_tree[cur_vertex] = l
        return

    mid = (l + r) // 2
    build(l, mid, 2 * cur_vertex)
    build(mid, r, 2 * cur_vertex + 1)

    segment_tree[cur_vertex] = segment_tree[cur_vertex *
                                            2 + 1] + segment_tree[cur_vertex * 2]


def update(cur_vertex, l, r, pos, x):
    if l + 1 == r:
        segment_tree[cur_vertex] = x
        return

    mid = (l + r) // 2

    if pos < mid:


build(0, len(array), 0)
