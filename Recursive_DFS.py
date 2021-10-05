

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}
def recursive_dfs(v,discovered): # 이미 발견한 노드는 담아놓았다가 나중에 체크할때 사용
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered: # 이미 방문한걸로 침
            discovered = recursive_dfs(w, discovered)
    return discovered
print(recursive_dfs(1, []))