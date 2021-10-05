import collections
import heapq

INF = int(1e9)


def dijkstra(graph, src, dst):
    n = len(graph)
    dist = [INF for i in range(n + 1)]
    dist[src] = 0  # 출발노드는 자기 자신이므로 거리는 0이다.
    Q = [(0, src)]
    while Q:
        w, x = heapq.heappop(Q)
        if dist[x] < w:
            continue
        for nnode, ndist in graph[x]:
            ndist += w
            if ndist < dist[nnode]:  # 초기 셋팅은 무한대로 되어 있다.
                dist[nnode] = ndist
                heapq.heappush(Q, (ndist, nnode))

    return dist[dst]


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for src, dst, cost in fares:
        graph[src].append((dst, cost))
        graph[dst].append((src, cost))
    cost = dijkstra(graph, s, a) + dijkstra(graph, s, b)
    for i in range(n + 1):
        if s != i:
            cost = min(cost, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))
    return cost


graph = [[]]


def preprocess(n, fares):
    global graph
    graph = [[] for i in range(n + 1)]

    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])


def dijkstra2(src, dst):
    global graph
    n = len(graph)
    table = [INF for i in range(n)]
    table[src] = 0
    pq = [[0, src]]

    while pq:
        w, x = heapq.heappop(pq)

        if table[x] < w: continue

        for item in graph[x]:
            nx, ncost = item[0], item[1]
            new_cost = ncost + w
            if new_cost < table[nx]:
                table[nx] = new_cost
                heapq.heappush(pq, [new_cost, nx])

    return table[dst]


def solution2(n, s, a, b, fares):
    preprocess(n, fares)
    cost = INF

    for i in range(1, n + 1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return cost


result = solution2(6, 4, 6, 2,
                   [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                    [1, 6, 25]])
result2 = solution2(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
print(result)
print(result2)
