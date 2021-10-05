import itertools
from typing import List


# dfs 탐색으로 값을 하나씩 제거하며 완성하는 알고리즘

# 순열 수식    n! /  (n-r)!
def permutation(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])
            print(f'results : {results} dfs 종료')
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            print(f'elements : {elements}, prev_elements : {prev_elements}, next_elements : {next_elements}, dfs 호출')
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


print(permutation([1, 2, 3]))


# dfs로 값을 하나씩 추가하며 방문을 체크하며 순열을 완성하는 알고리즘

# def gen_permutation(n, depth, P, arr):
#     result = []
#     if depth == n:
#         return [P] # 2차원 리스트
#     else:
#         for i, v in enumerate(arr):
#             if chosen[i] == True:
#                 continue
#             chosen[i] = True
#             # 2차원리스트끼리 합침
#             result += gen_permutation(n, depth + 1, P + [v], arr)
#             chosen[i] = False
#     return result # 2차원리스트 반환
#
#
# arr = [1, 2, 3]
# chosen = [False for _ in range(len(arr))]
# print(gen_permutation(3, 0, [], arr))

# 순열 itertools에 있는 permutation메서드 사용하는 경우

def permute(self, nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))


print(permutation([1, 2, 3]))
