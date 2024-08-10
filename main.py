from itertools import combinations

def combinate(S, k):

    k = int(k)
    s = sorted(S)

    for i in range(k):
        p = combinations(s, i+1)
        
        for j in (p):
            print(''.join(j))

if __name__ == '__main__':
    S, k = list(input().split())
    result = combinate(S, k)