"""
문제

2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라.

해설

브루트포스로 푸는 단순 문제

"""
from typing import List


def letterCombinations(digits: str) -> List[str]:
    #  중첩함수로 부모변수를 공유함
    def dfs(index, path):
        # 끝나는 시점은 입력으로 주어진 길이와 탐색한 갯수가 같을 때
        if len(path) == len(digits):
            result.append(path)
            return
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
           }
    result = []
    dfs(0, "")
    return result
result = letterCombinations("23")
print(result)