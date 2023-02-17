def find_third_point(first, second, x3):
    x1 = first[0]
    y1 = first[1]
    x2 = second[0]
    y2 = second[1]
    y_diff = y2 - y1
    x_diff = x2 - x1
    slope = y_diff / x_diff  # Find slope
    y_intercept = y1 - slope*x1  # Find y intercept
    y3 = y_intercept + slope*x3  # Find y3
    print(y3)
    return y3


if __name__ == "__main__":
    y = find_third_point([2, 5], [3, 2.2], 3)
