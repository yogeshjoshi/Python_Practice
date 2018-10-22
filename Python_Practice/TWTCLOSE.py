N, K = input().split()
N = int(N)
K = int(K)
tweets = []
for _ in range(N):
    tweets.append(0)
for _ in range(K):
    action = input().split()
    if action[0] == 'CLOSEALL':
        pass
    else:
        x = int(action[1])

    if action[0] == 'CLICK' and tweets[x-1] == 0:
        tweets[x-1] = 1
    elif action[0] == 'CLICK' and tweets[x-1] == 1:
        tweets[x-1] = 0
    else:
        for i in range(N):
            tweets[i] = 0
    print(sum(tweets))
# link of codechef https://www.codechef.com/problems/TWTCLOSE
