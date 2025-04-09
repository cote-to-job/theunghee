def solution(n):
    dp = [0, 1, 1] + [0] * (n - 2) # n은 2 이상이기에 2까지 배열에 저장
    for i in range(3, n + 1): # 계산하여 리스트에 저장
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567
