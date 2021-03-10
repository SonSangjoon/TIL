# https://www.acmicpc.net/problem/9095
# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# 출력
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
# f(n) = f(n-1) + f(n-2) + f(n-3)
# 2 - 11 2
# 3 - 111 12 21 3

N = int(input())
lst = [int(input()) for _ in range(N)]


def dinamic(n):
    ans = [0,1,2,4]
    if n <= 3:
        return ans[n]
    else:
        return dinamic(n-1) + dinamic(n-2) + dinamic(n-3)

for i in lst:
    print(dinamic(i))

