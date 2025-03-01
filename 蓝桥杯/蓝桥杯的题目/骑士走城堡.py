import sys

# 增加递归深度限制，防止递归过深导致程序崩溃
sys.setrecursionlimit(1500000)

# 输入棋盘大小
n = int(input())
# 输入每行的限制步数
hang = list(map(int, input().split()))
# 输入每列的限制步数
lie = list(map(int, input().split()))

# 计算目标步数，每n行每n列，总步数是n² - 1（因为起点也算一步）
tar = n * n - 1

# 定义四个方向（右、下、上、左），让骑士可以正常移动
dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# 初始化访问标记矩阵，防止重复访问
vis = [[0] * n for _ in range(n)]
# 用于记录路径
path = ""
# 标记是否找到有效路径
found = False

# 定义深度优先搜索函数
def dfs(x, y, current_path, steps):
    global found
    # 如果已经找到路径，直接返回
    if found:
        return

    # 标记当前位置已访问
    vis[x][y] = 1
    # 减少当前行和列的剩余步数
    hang[x] -= 1
    lie[y] -= 1

    # 检查是否满足当前行和当前列的条件
    if hang[x] >= 0 and lie[y] >= 0:
        # 如果当前行必须耗尽，检查前面的所有行是否已经满足
        for i in range(x):
            if hang[i] != 0:
                # 如果前面的行未满足，恢复状态并返回
                vis[x][y] = 0
                hang[x] += 1
                lie[y] += 1
                return
        # 检查前面的列是否满足
        for i in range(y):
            if lie[i] != 0:
                # 如果前面的列未满足，恢复状态并返回
                vis[x][y] = 0
                hang[x] += 1
                lie[y] += 1
                return

    # 如果到达右下角
    if x == n - 1 and y == n - 1:
        # 检查是否满足总步数和行列限制
        if steps == tar and sum(hang) == 0 and sum(lie) == 0:
            # 如果满足，记录路径并标记找到
            nonlocal path
            path = current_path
            found = True
        # 恢复状态
        vis[x][y] = 0
        hang[x] += 1
        lie[y] += 1
        return

    # 尝试四个方向移动
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        # 检查是否在棋盘内且未访问过
        if 0 <= nx < n and 0 <= ny < n:
            if not vis[nx][ny] and hang[nx] > 0 and lie[ny] > 0:
                # 递归搜索下一个位置
                dfs(nx, ny, f"{current_path}/{nx * n + ny}", steps + 1)
                # 如果找到路径，直接返回
                if found:
                    return
    # 回溯，恢复状态
    vis[x][y] = 0
    hang[x] += 1
    lie[y] += 1

# 从起点 (0, 0) 开始搜索
dfs(0, 0, "0", 1)
# 输出找到的路径
print(path)
