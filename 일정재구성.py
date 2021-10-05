import collections
from typing import List


def findItinerary1(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    # for key, value in graph.items():
    #     print(key, value)
    route = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop(0))  # 시간 복잡도 O(N)이다
        route.append(node)

    dfs('JFK')
    return route[::-1]


# print(findItinerary1([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))


def findItinerary2(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse=True):  # 순서를 역수으로 해놓고 뒤에서 끄집어 낸다
        graph[a].append(b)

    # for a, b in graph.items():
    #     print(a, b)
    route = []

    def dfs(node):
        while graph[node]:
            dfs(graph[node].pop())  # 시간복잡도 O(1)이다. 뒤에서 POP하기 때문에
        route.append(node)

    dfs('JFK')
    return route[::-1]


# print(findItinerary2([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))

def findItinerary3(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    for k, v in graph.items():
        print(k, v)
    stack = ['JFK']
    route = []

    def iterative():
        while stack:  
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            # 모든 스택을 쌓은후에 풀어낸다
            route.append(stack.pop())
    iterative()
    return route[::-1]


print(findItinerary3([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
