
"""
정수삼각형
"""


# def solution(triangle):
#     answer = 0
#     s = len(triangle)
#     graph = [[0] * s for _ in range(s)]
#     graph[0][0] = triangle[0][0]
#     maxV = -1e9
#
#     for i in range(s-1):
#         for j in range(s):
#             graph[i+1][j]=triangle[i+1][j]+graph[i][j]
#             maxV=max(maxV, graph[i][j])
#     return maxV

def solution(triangle):
    # dp 테이블 초기화
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    # 거쳐간 숫자의 최댓값 구하기
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    return max(dp[-1]) # dp 테이블의 마지막 원소들 중 최댓값 반환

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))