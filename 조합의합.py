from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    # 각각의 인자는 csum은 타켓수이고, index는 0부터 시작하고 path는 방문한 노드과정이다.
    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        # 중복이 가능하므로 index가 그대로 들어간다 -> 중복이 아니라면 i + 1로 dfs탐색한다.
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


print(combinationSum([2, 3, 6, 7], 7))
