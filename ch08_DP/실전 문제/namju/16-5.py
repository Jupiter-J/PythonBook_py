

"""
못생긴 수
10
4
"""

# """
# ugly = [2,3,5]
# [1,2,3,4,5,6,8,9,12,15]
#
# """
#
# n=int(input())
# ugly = [2,3,5]
# answer = [1]
# cnt=1
#
# while True:
#     i=2
#     for x in ugly: # [2,3,5]
#         if i % x in ugly:
#             answer.append(i)
#         i += 1
#         cnt += 1
#     if cnt==n:
#         print(answer)
#         break
# print(answer[n-1])


n = int(input())
ugly = [False]*1001
ugly[1] = True

for i in range(2, 1001):
    if i%2==0:
        ugly[i] = True
    elif i%3==0:
        ugly[i] = True
    elif i%5==0:
        ugly[i] = True

answer = []
for i in range(len(ugly)):
    if ugly[i] == True:
        answer.append(i)
print(answer[n-1])






