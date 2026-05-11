# -*- coding: utf-8 -*-
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    
    idx = 1
    while idx < len(input_data):
        r = int(input_data[idx])
        c = int(input_data[idx+1])
        v = int(input_data[idx+2])
        if r == 0 and c == 0 and v == 0:
            break
        grid[r][c] = v
        idx += 3
        
    # dp[k][i][j] 表示两条路径都走了 k 步，第一条路行坐标为 i，第二条路行坐标为 j 时取得的最大数之和
    # k = r1 + c1 = r2 + c2。 范围 2 到 2*n
    # 数组大小 (2*n+1) x (n+1) x (n+1)
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2 * n + 1)]
    
    for k in range(2, 2 * n + 1):
        for i1 in range(1, n + 1):
            for i2 in range(1, n + 1):
                j1 = k - i1
                j2 = k - i2
                
                # 检查列坐标合法性
                if 1 <= j1 <= n and 1 <= j2 <= n:
                    # 确定当前格子的值
                    current_val = grid[i1][j1]
                    if i1 != i2: # 如果不在同一个格子上
                        current_val += grid[i2][j2]
                    
                    # 状态转移：四种来源
                    # 1. 都在上方下来 (i1-1, i2-1)
                    # 2. 第一条上方，第二条左方 (i1-1, i2)
                    # 3. 第一条左方，第二条上方 (i1, i2-1)
                    # 4. 都在左方下来 (i1, i2)
                    dp[k][i1][i2] = max(
                        dp[k-1][i1][i2],
                        dp[k-1][i1-1][i2],
                        dp[k-1][i1][i2-1],
                        dp[k-1][i1-1][i2-1]
                    ) + current_val
                    
    print(dp[2 * n][n][n])

if __name__ == "__main__":
    solve()
