"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(sr, sc)]
        visited = {(sr, sc)}
        color = image[sr][sc]
        while q:
            x, y = q.pop()
            image[x][y] = newColor
            for dirx, diry in directions:
                tx, ty = x + dirx, y + diry
                if 0 <= tx < m and 0 <= ty < n and image[tx][ty] == color and (tx, ty) not in visited:
                    q.append((tx, ty))
                    visited.add((tx, ty))
        return image