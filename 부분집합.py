from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    result = []

    # 압서 조합과 달리 매번 결과를 추가 해야한다.
    def dfs(index, path):
        result.append(path)
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])
    dfs(0,[])
    return result


print(subset([1, 2, 3]))
