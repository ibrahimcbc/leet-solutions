class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix[0])-1
        up=0
        down=len(matrix)-1
        while down>=up:
            row=(up+down)//2
            if matrix[row][0]>target:
                down=row-1
            elif matrix[row][-1]<target:
                up=row+1
            else:
                break
        while right>=left:
            column=(left+right)//2
            if matrix[row][column]>target:
                right=column-1
            elif matrix[row][column]<target:
                left=column+1
            else:
                return True
        return False
        