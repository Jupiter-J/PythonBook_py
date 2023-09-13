

"""
편집거리

삽입 : 문자 추가
삭제 : 문자 삭제
교체 : 문자를 교체
SUNDAY
SATURDAY

SUNDAY #UNㅎ
SATURDAY #ATUR
S[A삽입][N삭제][T추가]U[R추가]DAY

같은 문자열이 있는지 확인 + 같은 문자열 따로 save[]=저장 // s2에 맞춰 문자열 순서 고려해야함(이동때문에)
save에 S2와 같은문자가 있으면 그대로 answer[] append (위치가 다르면 이동이됨!)
save에 없으면
"""

s1 = input() #sunday
s2 = input() #saturday
save = [] # SAYDU
answer = []
for i in range(len(s2)):
    if s2[i] in s1:
        save.append(s2[i])
# save에 중복 문자 들어옴 // 테케에서 오류남
save = set(save)
save = list(save)
cnt=0
for c in s2:
    if c in save:
        answer.append(c)
    else:
        answer.append(c)
        cnt+=1
print(cnt)




