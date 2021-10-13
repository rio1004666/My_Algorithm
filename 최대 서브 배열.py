
from typing import List


def Mamximum_Sub_Array(array: List[int]):
    sum: List[int] = [array[0]] # 타입선언과 동시에 첫원소 삽입
    # 여기서 중요한것은 음수는 합하지 않고 그 원소 그대로 넣어서
    # 그 전의 원소와는 연결고리를 끊는것이다

    for idx in range(1, len(array)):
        sum.append(array[idx] + (sum[idx -1] if sum[idx -1] > 0 else 0))
    return max(sum) # 서브 배열 합중 최댓값을 선택한다.
print(Mamximum_Sub_Array([-2 ,1 ,-3 ,4 ,-1 ,2 ,1 ,-5 ,4]))
