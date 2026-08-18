class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            high = len(matrix[0])
            low = 0 # to go through all the rows
            while (low <= high) and low < len(matrix[0]):
                mid = (high + low)//2
                l = matrix[i][mid]

                if l < target:
                    low = mid + 1
                elif l > target:
                    high = mid - 1
                else:
                    return True 
        
        return False