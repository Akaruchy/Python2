# Задача 1.
# Напишите функцию для транспонирования матрицы


def my_func(my_matrix):
    rows = len(my_matrix)
    cols = len(my_matrix[0])
    transp_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transp_matrix[j][i] = my_matrix[i][j]
    return transp_matrix


matrix = [[11, 32, 53], [1, 42, 9], [7, 12, 45]]
print(my_func(matrix))