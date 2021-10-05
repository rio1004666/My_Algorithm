import itertools
from typing import List


# dfs를 활용한 combination
# 조합 수식    n! / (r! * (n-r)!)
def combination(n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: n, k: int):
        if k == 0:
            results.append(elements[:])
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    print(results)
    return results


combination(4, 2)


# itertools 모듈 사용

def combine(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))


print(combine(4, 2))
