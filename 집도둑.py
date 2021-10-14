import collections
from typing import List


def rob(nums: List[int]) -> int:
    # 1. 재귀 구조  브루트 포스

    def _rob(i: int) -> int:
        if i < 0:
            return 0
        return max(_rob(i - 1), _rob(i - 2) + nums[i])

    return _rob(len(nums) - 1)


def rob2(nums: List[int]) -> int:
    # 2. 다이나믹 프로그래밍 타블레이션(상향식 풀이)
    if not nums: # 리스트에 아무것도 없다면 0 리턴
        return 0
    if len(nums) <= 2:  # 갯수가 2개뿐이라면 두개중 최댓값 리턴
        return max(nums)
    dp = collections.OrderedDict()  # 순서를 유지하는 딕셔너리

    dp[0], dp[1] = nums[0], max(nums[0], nums[1])  # 첫번째값과 두번째 값 둘 중 최대가 선택되어야 최댓값이 된다.

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp.popitem()[1]


print(rob2([1, 2, 3, 1]))
