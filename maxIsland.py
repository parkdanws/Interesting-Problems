"""
June 6 2018

Leetcode 695 Max area of island

Given a non-empty 2D array 'grid' of 1/0 (List of lists)
Define: Island-- group of 1's connected vertically/horizontally.
Not diagonally.
Find: maximum area of island in given array

EG:
0 0 0 0 
1 0 1 0
1 1 1 0
0 0 0 1

Max size is 5
"""

"""
Intuition: iterate every tile, keeping track of a dictionary
of visited tiles.
When we meet a '1', perform dfs on it.
"""
def main():
    g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    g2 = [[0,0,0,0,0]]
    g3 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    g4 = [[1]]
    print (Solution().maxAreaOfIsland(g4))



class Solution(object):
    def maxAreaOfIsland(self,grid):
        vis = set() 
        maxSize = 0
        getTile = self.nextTile(grid)

        for i,j in getTile:
            if grid[i][j] == 1 and (i,j) not in vis:
                maxSize = max(self.dfs(grid,i,j,vis),maxSize)

        return maxSize

    def dfs(self,grid,i,j,vis):
        """
        Thought: good catch with the grid[i][j] == 0, becaue
        getneighbors will not catch that, even though the
        maxareaofisland will
        """
        if (i,j) in vis or grid[i][j] == 0:
            return 0

        vis.add((i,j))
        ret = 1
        
        for ni,nj in self.getNeighbors(grid,i,j):
            ret += self.dfs(grid,ni,nj,vis)
        return ret
        

    def getNeighbors(self,grid,i,j):
        """
        returns neighbors even those that aren't 1's lol
        Thought: tiny inputs of size 1x1 will require constraints
        on all 4 sides. therefore, should not use elif
        """
        ret = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        if i == 0:
            ret.remove((i-1,j))
        if i == len(grid) - 1:#originally elif. see lesson
            ret.remove((i+1,j))
        if j == 0:
            ret.remove((i,j-1))
        if j == len(grid[0])-1:
            ret.remove((i,j+1))
        return ret
    

    def nextTile(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                yield i,j


class leetSoln(object):
    """
    Solution from leetcode. commentary mine
    https://leetcode.com/articles/max-area-of-island/#
    """
    def maxAreaOfIsland(self,grid):
        seen = set()
        def area(r,c):
            """
            if not:
            row is greater than or equal to 0 and less than len of grid 
            (num rows)
            and column is gtE 0 or less than len grid[0] (numcols)
            (these first two verify within bounds)

            and (row,column) has not been visited
            and the value in [r][c] is 1 (lol eval as boolean)
            If these conditions are not met, return 0
            """
            if not( 0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r,c) not in seen and grid[r][c]):
                return 0
            seen.add((r,c)) #conditions are met. add to visited

            """
            recursively sum. similar to what I did
            """
            return (1 + area(r+1,c) + area(r-1,c) +
                    area(r,c-1) + area(r,c+1))

        """
        holy crap what is this
        not even using colons?
        Sooo this format will apparently return a generator object
        and the return statement will cause it to run
        what the hell
        """
        return max(area(r,c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

    """
    Instead of keeping a visited set, one could also
    just replace the seen '1' values with a 0
    """
if __name__ == "__main__":
    main()
