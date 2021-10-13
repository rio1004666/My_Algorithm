# 피보나치 수열 구현
# 재귀 구조 브루트 포스
import collections


def fib(N: int) -> int:
    if N <= 1:
        return N
    return fib(N - 1) + fib(N - 2)


# result = fib(10)
# print(result)

# 메모이제이션 (하향식 풀이)
dp = collections.defaultdict(int)  # 키값이 생성될때마다 항상 0이 셋팅된다. 널값을 무시하게되어서 아주 편리한 라이브러리다


def fib2(N: int) -> int:
    if N <= 1:
        return N

    if dp[N]:  # 이미 값이 있다면 더이상 재귀구조로 들어가지 않는다는 것이 다이나믹 프로그래밍의 중복된 하위구조이다.
        return dp[N]
    dp[N] = fib(N - 1) + fib(N - 2)
    return dp[N]


# result = fib2(10)
# print(result)

# 타블레이션 (상향식 풀이)

def fib3(N: int) -> int:
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[N]


# result = fib3(10)
# print(result)

# 두 변수만 사용해도 된다 => 공간복잡도 O(n) -> O(1)

def fib4(N: int) -> int:
    x, y = 0, 1
    for i in range(0, N):
        x, y = y, x + y
    return x


# 0-1 배낭문제
# 주어진 용량만큼 배낭에 채울 수 있는 최대 가격
# 그리디로 풀 수 없음 ( 짐을 쪼갤 수 없기 떄문에 )
# 중복된 하위 문제들 속성을 이용하여 다이나믹 프로그래밍으로 푼다.

cargo = [
    (4, 12), # 0
    (2, 1), # 1
    (10, 4), # 2
    (1, 1),
    (2, 2)
]

# 타블레이션(상향식풀이)를 활용한 0-1 배낭문제
def zero_one_knapspack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):  # 6 x 16 기준점을 세운다 cargo로 5개짐이며 +1로 인덱스를 맞추고
        pack.append([])  # 0개의 짐을 기준으로 채울 수 있는 용량을 넣어본다.
        for c in range(capacity + 1):  # capacity 15kg + 1 로 인덱스를 맞춘다.
            if i == 0 or c == 0: # 짐이 0개거나 용량이 0이면 무조건 0으로 셋팅된다 처름에는
                pack[i].append(0)
                # i == 1 이라면 12kg의 4달러이다 c가 12가 되는 순간 조건을 만족하므로 이 조건문을 들어간다.
                #
            elif cargo[i - 1][1] <= c:
                pack[i].append( # 첫번째배낭에다가 전의 것과 비교하여 더 비싼 배낭을 선택하게 된다.
                    max(
                        cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                        # 4 +  현재 12kg이고 지금 용량이 12kg이라면 꽉차기 때문에 현재 배낭의 용량을 최댓값으로 설정한다
                        pack[i - 1][c] # 이미 저장해두었던 용량 12kg에 대한 가치와 비교해야한다
                        # 13kg이라면? 13-12kg = 1kg이므로 이미 배낭에 저장된 1kg용량의 최댓값을 더하고 그 전의 13kg가치와 비교해본다.
                        # 14kg이라면? 14-12kg = 2kg이므로 이미 배낭에 저장된 2kg용량의 최댓값을 더하고 그 전의 14kg가치와 비교해본다..
                    )
                )
            else: # 만약 12kg보다 크다면 조건을 만족하지 않으므로 전에 저장해두었던 값을 그대로 넣어버린다.
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1] # 원하는 용량에 대한 최대값을 구한다.


print(zero_one_knapspack(cargo))
