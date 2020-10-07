# Find the maximum connected colors in a given table
# 10010
# 11100   -> has to return 5
# 01000
# 04.09.2020 -> TechLead CoderPro free overview questions

# I couldn't come up with a solution for this one so the Grid class belongs to TechLead
# time complexity -> we only visit each node once thus O(n)
# space complexity -> total number of cells O(n)
class Grid:
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        max_n = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                # max_n = max(max_n, self.dfs(x, y, {}))
                max_n = max(max_n, self.dfsIterative(x, y, {}))
        return max_n

    def colorAt(self, x, y):
        if x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid):
            return self.grid[y][x]
        return -1

    def neighbors(self, x, y):
        POSITIONS = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        n = []
        for pos in POSITIONS:
            if self.colorAt(x + pos[0], y + pos[1]) == self.colorAt(x, y):
                n.append((x + pos[0], y + pos[1]))
        return n

    # recursive solution
    def dfs(self, x, y, visited):
        key = str(x) + ',' + str(y)
        if key in visited:
            return 0
        visited[key] = True
        result = 1
        for neighbor in self.neighbors(x, y):
            result += self.dfs(neighbor[0], neighbor[1], visited)
        return result

    # iterative solution
    def dfsIterative(self, x, y, visited):
        stack = [(x, y)]
        result = 0
        while len(stack) > 0:
            (x, y) = stack.pop()
            key = str(x) + ',' + str(y)
            if key in visited:
                continue
            visited[key] = True

            result += 1
            for neighbor in self.neighbors(x, y):
                stack.append(neighbor)

        return result


grid = [[1, 0, 0, 1],
        [1, 1, 1, 0],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())
# 5
