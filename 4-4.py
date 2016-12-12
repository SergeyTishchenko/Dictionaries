def is_magic_square(square_matrix):
    magic_number = sum(square_matrix[0])
    size_of_matrix = len(square_matrix[0])

    for row in square_matrix:
        if sum(row) != magic_number:
            return False

    for columns in zip(*square_matrix):
        if magic_number != sum(columns):
            return False

    if sum(square_matrix[x][x] for x in range(size_of_matrix)) != magic_number:
        return False

    if magic_number != sum(square_matrix[x][size_of_matrix-1 - x] for x in range(size_of_matrix)):
        return False
    return True

if __name__ == '__main__':
    print(is_magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print(is_magic_square([[2, 3, 4, 5], [4, 4, 4], [5, 5, 5]]))
