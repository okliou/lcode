class Solution:
    """
    给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。

    说明：
    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

    给定 matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],

    原地旋转输入矩阵，使其变为:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
    """

    def rotate(self, matrix):
        """
        思路：观察input和output的矩阵，可以将旋转90度拆分为2步：第1步，沿对角线调换2边的元素，第2步，沿着竖直方向的中线，调换左右两边的元素。
        第一步，根据对角线，找对应位置，互换两个数字的值。
        第二步，对每一行数字，根据中线左右翻转
        
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) <= 0:
            return

        h = len(matrix)
        w = len(matrix[0])
        for i in range(h):
            for j in range(i + 1, w):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(h):
            # for j in range(w // 2):
            #     matrix[i][w - 1 - j], matrix[i][j] = matrix[i][j], matrix[i][w - 1 - j]
            matrix[i].reverse()
        return matrix


if __name__ == '__main__':
    print(Solution().rotate([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))