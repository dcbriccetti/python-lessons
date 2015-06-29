class GridMutator(object):
    def generateNext(self, grid):
        return [[self._isNewCellOn(grid,r,c) for c in range(len(grid))]
            for r in range(len(grid[0]))]

    def _isNewCellOn(self, grid, row, col):
        neighbors = self._countNeighbors(grid, row, col)
        return neighbors == 3 if not grid[row][col] else neighbors in (2,3)

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
