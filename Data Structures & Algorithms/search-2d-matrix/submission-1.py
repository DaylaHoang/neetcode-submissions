class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, column = mid // columns, mid % columns
            if target > matrix[row][column]:
                left = mid + 1
            elif target < matrix[row][column]:
                right = mid - 1
            else: return True
        return False