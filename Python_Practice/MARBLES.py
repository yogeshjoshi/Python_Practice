t = int(input())
factorial_collection = [1]


def fact(n, k):
    prod = 1
    k = min(k-1, n-k)
    for i in range(1, k+1):
        prod *= n-i
        prod //= i
    return prod


while t > 0:
    N, K = input().split()
    N = int(N)
    K = int(K)
    if N == K:
        result = 1
    elif N < K:
        result = 1
    else:
        result = fact(N, K)
    print(result)
    t -= 1


