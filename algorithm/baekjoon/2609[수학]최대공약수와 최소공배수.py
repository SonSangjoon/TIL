# 유클리드 호재법
# https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95#%EC%A6%9D%EB%AA%85_2
def gcd(m, n):
    while n != 0:
        t = m % n
        m, n = n, t
    return m


n, m = map(int, input().split())
gcf = gcd(n, m)
print(gcf)
print(gcf * (n // gcf) * (m // gcf))
