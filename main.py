class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack[-1]
                grid[y][x] = "0"
                if x - 1 > 0 and grid[y][x - 1] != "0":
                    stack.append((x - 1, y))
                elif y - 1 > 0 and grid[y - 1][x] != "0":
                    stack.append((x, y - 1))
                elif x + 1 < len(grid[0]) and grid[y][x + 1] != "0":
                    stack.append((x + 1, y))
                elif y + 1 < len(grid) and grid[y + 1][x] != "0":
                    stack.append((x, y + 1))
                else:
                    stack.pop()

        num_islands = 0

        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] != "0":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
