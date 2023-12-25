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

if __name__ == "__main__":
            main()