from collections import deque
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
def iterative_bfs(start_v):
    discovered = [start_v]
    q = deque([start_v])
    while q:
        v = q.popleft()
        for w in graph[v]:
            if not w in discovered:
                discovered.append(w)
                q.append(w)
    return discovered
print(iterative_bfs(1))


