#Soluciones por Pablo Moreno Moreu, Arnau Neches Vila, Carlos Fernandez-LLebrez Acedo
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        #Igual que el 62 (casi) hay que modificar la primera fila y columna primero, luego cogemos el camino minimo

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]