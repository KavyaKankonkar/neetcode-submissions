class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        

        for i in range(row):
            k=0
            col=len(matrix[i])
            l=col-1
            while(k<=l):
                mid=k+((l-k)//2)
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    l=mid-1
                else:
                    k=mid+1
        
        return False
