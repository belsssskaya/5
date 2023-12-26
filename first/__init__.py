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
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass

if __name__ == "__main__":
            main()