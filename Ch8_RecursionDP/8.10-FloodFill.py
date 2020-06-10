def floor_fill(image, sr, sc, newColor):
    original_color = image[sr][sc]
    if original_color == newColor:
        return image

    def helper(sr, sc):
        if image[sr][sc] == original_color:
            image[sr][sc] = newColor
            if sr - 1 >= 0:
                helper(sr-1, sc)
            if sr + 1 < len(image):
                helper(sr+1, sc)
            if sc + 1 < len(image[0]):
                helper(sr, sc+1)
            if sc - 1 >= 0:
                helper(sr, sc-1)

    helper(sr, sc)
    return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(floor_fill(image, sr, sc, newColor))
