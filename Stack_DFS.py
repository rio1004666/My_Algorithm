

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
def iterative_dfs(start_v): # 이미 발견한 노드는 담아놓았다가 나중에 체크할때 사용
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered: # 방문을 하지 않았다면
            discovered.append(v) # 방문했다고 표현
            # 그리고 인접리스트 순회
            for w in graph[v]: # 인접한 노드 담는다
                stack.append(w) # 마지막에 있는것부터 꺼내므로 거꾸로가 된다 재귀적인 것보다
    return discovered

print(iterative_dfs(1))