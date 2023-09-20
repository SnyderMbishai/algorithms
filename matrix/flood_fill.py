class Solution:
    def floodFill(self, image: list, sr: int, sc: int, color: int):
        target_pixel = image[sr][sc]
        self.dfs(image, sr, sc, target_pixel, color)
        return image

    def dfs(self, image, sr, sc, start_color, new_color):
        # print(sr, sc)
        # print(image)
        try:
            if (
                sr < 0
                or sr > (len(image[0]) - 1)
                or sc < 0
                or sc > (len(image) - 1)
                or image[sr][sc] != start_color
            ):
                return

            image[sr][sc] = new_color
            self.dfs(image, sr + 1, sc, start_color, new_color)
            self.dfs(image, sr - 1, sc, start_color, new_color)
            self.dfs(image, sr, sc + 1, start_color, new_color)
            self.dfs(image, sr, sc - 1, start_color, new_color)
        except Exception as e:
            breakpoint()
            print(sr, sc, "===", len(image[0]) - 1)


if __name__ == "__main__":
    print("hey")
    a = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    a1 = Solution().floodFill(a, 1, 1, 2)
    print(a1)
