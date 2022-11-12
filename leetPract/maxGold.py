
#summits solution
def maxGold(grid):
    m = len(grid)
    n = len(grid[0])

    def dfs(x, y, path):
        if not (0 <= x < n) or not (0 <= y < m) or (x, y) in path or grid[y][x] == 0:
            return 0
        path.add((x, y))
        maxPath = 0
        # can potentially traverse entire grid
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):#goes up down left right

            maxPath = max(maxPath, dfs(x + dx, y + dy, path))

        path.remove((x, y))
        return maxPath + grid[y][x]
    res = 0
    for y in range(m):
        for x in range(n):
            path = set()  # tuples of (x,y)
            res = max(res, dfs(x, y, path))
    return res


#
#
if __name__ == "__main__":
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    print(maxGold(grid))
    grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    print(maxGold(grid))
