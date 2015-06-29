class GridMutator(object):
    def generateNext(self, grid):
        (ROWS, COLS) = (len(grid), len(grid[0]))
        nextGrid = [[False for r in range(ROWS)] for c in range(COLS)]
        for row in range(ROWS):
            for col in range(COLS):
                neighbors = self._countNeighbors(grid, row, col)
                nextGrid[row][col] = neighbors == 3 if not grid[row][col] \
                    else neighbors in (2,3)
        return nextGrid

    def _countNeighbors(self, grid, row, col):
        (ROWS, COLS) = (len(grid), len(grid[0]))
        neighbors = 0
        if row > 0: # Look above unless at top
            if col > 0 and grid[row-1][col-1]: neighbors += 1
            if grid[row-1][col]: neighbors += 1
            if col < COLS-1 and grid[row-1][col+1]: neighbors += 1

        # Look at same row
        if col > 0 and grid[row][col-1]: neighbors += 1
        if col < COLS-1 and grid[row][col+1]: neighbors += 1

        if row < ROWS-1: # Look below unless at bottom
            if col > 0 and grid[row+1][col-1]: neighbors += 1
            if grid[row+1][col]: neighbors += 1
            if col < COLS-1 and grid[row+1][col+1]: neighbors += 1

        return neighbors
