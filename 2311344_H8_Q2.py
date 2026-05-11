# -*- coding: utf-8 -*-
import sys

def solve():
    # 读取 M, N, K
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m = int(input_data[0])
    n = int(input_data[1])
    k = int(input_data[2])
    
    peanuts = []
    idx = 3
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            val = int(input_data[idx])
            if val > 0:
                peanuts.append({'val': val, 'x': i, 'y': j})
            idx += 1
            
    # 按花生数量从大到小排序
    peanuts.sort(key=lambda x: x['val'], reverse=True)
    
    total_peanuts = 0
    current_time = 0
    curr_x, curr_y = 0, 0 # 初始位置在路边
    
    for i in range(len(peanuts)):
        p = peanuts[i]
        
        # 计算到达该植株所需的时间
        if i == 0:
            # 第一步：从路边跳到第一行的某颗植株
            # 时间 = 行座标 (x) + 采摘 (1)
            travel_time = p['x']
        else:
            # 后续：从上一棵植株跳到这棵植株
            # 时间 = 曼哈顿距离 (|x1-x2| + |y1-y2|) 
            travel_time = abs(p['x'] - curr_x) + abs(p['y'] - curr_y)
            
        # 还要考虑采摘的时间和返回路边的时间
        harvest_time = 1
        return_time = p['x']
        
        needed_time = travel_time + harvest_time + return_time
        
        if current_time + needed_time <= k:
            # 如果剩余时间足够采摘并返回路边
            current_time += travel_time + harvest_time
            total_peanuts += p['val']
            curr_x, curr_y = p['x'], p['y']
        else:
            # 时间不够，停止采摘
            break
            
    print(total_peanuts)

if __name__ == "__main__":
    solve()
