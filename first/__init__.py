import random


def input_matrix(n):
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            try:
                value = int(input(f"Введите значение элемента [{i}][{j}]: "))
                row.append(value)
            except ValueError:
                print("Ошибка! Введите целочисленное значение!!!")
                return input_matrix()
        matrix.append(row)
    return matrix


def generate_matrix(n):
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    return matrix

def sum_matrices(matrix1, matrix2, n):
    sum_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(n)]
    return sum_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    while True:
        print("Меню:")
        print("1. Ввод матрицы вручную")
        print("2. Сгенерировать матрицу")
        print("3. Решение")
        print("4. Выход")
        choice = (input("Введите номер выбранного пункта: "))
        if choice == "1":
            n = int(input("Введите размерность матрицы: "))
            matrix1 = input_matrix(n)
            matrix2 = input_matrix(n)
            print("Матрица 1:")
            print_matrix(matrix1)
            print("Матрица 2:")
            print_matrix(matrix2)
        elif choice == "2":
            n = int(input("Введите размерность матрицы: "))
            matrix1 = generate_matrix(n)
            matrix2 = generate_matrix(n)
            print("Матрица 1:")
            print_matrix(matrix1)
            print("Матрица 2:")
            print_matrix(matrix2)
        elif choice == "3":
            try:
                sum_matrix = sum_matrices(matrix1, matrix2, n)
                print("Сумма матриц:")
                print_matrix(sum_matrix)
            except NameError:
                print("Ошибка! Пожалуйста, сначала выберите пункт 1 или 2 для ввода или генерации матрицы.")
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт из меню (1-4).")
            print()

if __name__ == "__main__":
            main()