def bubble_sort2d(matrix, N, M):
    for line in matrix:
        print(*line)
    print()
    for _ in range(N * M):
        for k in range(1, N * M):
            i_1 = k // M
            j_1 = k - i_1 * M
            i_2 = (k - 1) // M
            j_2 = (k - 1) - i_2 * M
            if matrix[i_2][j_2] > matrix[i_1][j_1]:
                matrix[i_2][j_2], matrix[i_1][j_1] = matrix[i_1][j_1], matrix[i_2][j_2]
                for line in matrix:
                    print(*line)
                print()
