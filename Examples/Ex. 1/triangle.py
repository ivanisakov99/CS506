def read_triangle(filepath):
    """
    Takes a file path.
    Returns a triangle represented as a list of lists.
    """

    triangle = []

    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            triangle.append(
                [int(char) for char in line.split(' ')]
            )

    return triangle


def do_fold(current_level, next_level):
    right_options = [0] + current_level
    left_options = current_level + [0]

    sum_from_the_right = map(
        lambda x: x[0] + x[1], zip(next_level, right_options))
    sum_from_the_left = map(
        lambda x: x[0] + x[1], zip(next_level, left_options))

    return list(map(lambda x: max(x), zip(
        sum_from_the_left, sum_from_the_right)))


def fold(triangle):
    """
    """
    current_level = triangle[0]

    for level in range(1, len(triangle)):
        next_level = triangle[level]
        current_level = do_fold(current_level, next_level)

    return current_level

if __name__ == '__main__':
    print('The max sum in the triangle is:', max(fold(read_triangle('./triangle.txt'))))
