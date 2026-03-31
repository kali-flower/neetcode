class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid) # number of sublists inside main list
        COLS = len(grid[0]) # length of first sublist 

        islands = 0


        def bfs(r, c): 
            q = deque() # initialize queue 
            grid[r][c] = "0" # mark it as visited 
            q.append((r, c)) # append it as a tuple 

            while q: 
                row, col = q.popleft() # get the coordinates of current value being processed 
                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col 
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"): 
                        continue 
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == "1": 
                    bfs(r, c)
                    islands += 1
        
        return islands 