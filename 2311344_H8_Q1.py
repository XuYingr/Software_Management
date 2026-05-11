# -*- coding: utf-8 -*-
import sys

def solve():
    # 读取第一行：N, M, T
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m, t = map(int, line1)
        
        # 读取第二行：SX, SY, FX, FY
        line2 = sys.stdin.readline().split()
        if not line2:
            return
        sx, sy, fx, fy = map(int, line2)
        
        # 初始化迷宫和访问状态
        # 坐标是从1开始的，所以我们创建一个 (n+1) x (m+1) 的数组
        maze = [[0] * (m + 1) for _ in range(n + 1)]
        visited = [[False] * (m + 1) for _ in range(n + 1)]
        
        # 读取 T 行障碍点
        for _ in range(t):
            tx, ty = map(int, sys.stdin.readline().split())
            if 1 <= tx <= n and 1 <= ty <= m:
                maze[tx][ty] = 1 # 1 表示障碍
                
        count = 0
        
        # 回溯搜索
        def dfs(x, y):
            nonlocal count
            # 到达终点
            if x == fx and y == fy:
                count += 1
                return
            
            # 四个方向移动
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                
                # 边界检查、障碍物检查、访问检查
                if 1 <= nx <= n and 1 <= ny <= m and maze[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny)
                    visited[nx][ny] = False # 回溯
        
        # 起点标记为已访问并开始搜索
        visited[sx][sy] = True
        dfs(sx, sy)
        
        print(count)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
