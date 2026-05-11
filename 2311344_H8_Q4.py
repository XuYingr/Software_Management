# -*- coding: utf-8 -*-
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m = int(input_data[0])
    n = int(input_data[1])
    
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    idx = 2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid[i][j] = int(input_data[idx])
            idx += 1
            
    # dp[k][i1][i2] 表示两条路径都走了 k 步，第一条路行坐标为 i1，第二条路行坐标为 i2 时取得的最大好感度之和
    # k = r1 + c1 = r2 + c2。 范围 2 到 m + n
    # 由于 m, n <= 50，dp 数组大小为 (m+n+1) x (m+1) x (m+1)
    dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + n + 1)]
    
    for k in range(2, m + n + 1):
        for i1 in range(1, m + 1):
            for i2 in range(1, m + 1):
                j1 = k - i1
                j2 = k - i2
                
                # 检查坐标合法性 (1-indexed)
                if 1 <= j1 <= n and 1 <= j2 <= n:
                    # 计算当前步的收益
                    # 除了起点(2步)和终点(m+n步)，题目要求不能经过同一个人
                    # 虽然 DP 会自动过滤，但逻辑上：如果 i1 == i2，则表示同一个人
                    val = grid[i1][j1]
                    if i1 != i2:
                        val += grid[i2][j2]
                    
                    # 状态转移，四种组合来源
                    dp[k][i1][i2] = max(
                        dp[k-1][i1][i2],     # 两个都从左边来 (j1-1, j2-1)
                        dp[k-1][i1-1][i2],   # 一路径从上过来，二路径从左过来
                        dp[k-1][i1][i2-1],   # 一路径从左过来，二路径从上过来
                        dp[k-1][i1-1][i2-1]  # 两个都从上面来 (i1-1, i2-1)
                    ) + val
                    
    # 最终结果在两条路径都到达 (m, n) 时
    print(dp[m + n][m][m])

if __name__ == "__main__":
    solve()
