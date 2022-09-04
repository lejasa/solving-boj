import sys
C = int(input())    # 테스트 케이스의 개수
s = []              # 점수
count = 0

while True:
    num = 0
    s.clear()
    if count == C: break
    else: 
        s.append(list(map(int,sys.stdin.readline().split())))
        N = s[0][0]    # 학생의 수
        score = s[0][1:N+1]
        count+=1
        ms = sum(score)/len(score)
        for k in score:
            if ms < k:
                num+=1
    print(f'{num/len(score)*100:.3f}%')