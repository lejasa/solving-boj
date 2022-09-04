from collections import Counter
import math
import sys
input = sys.stdin.readline
# 참고 : https://gorokke.tistory.com/126

def second_frequent(nums):
    counter = Counter(nums).most_common()
    if len(counter) > 1 and counter[0][1] == counter[1][1]:
        return counter[1][0]
    else:
        return counter[0][0]

N = int(input())

S = [int(input()) for _ in range(N)]
S = sorted(S)

print(f'{int(round(sum(S)/N,0)):.0f}')
print(S[len(S)//2])
print(second_frequent(S))
print(max(S)-min(S))