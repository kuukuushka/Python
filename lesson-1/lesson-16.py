# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row * col, end="\t")
#     print()


# N = int(input("Введите число N: "))
# for row in range(N + 1):
#     # for col in range(N + 1):
#     #     print(row + col, end="\t")
#     # print()


# for row in range(10):
#     for col in range(10):
#         print(row - col, end="\t")
#     print()



# N = int(input("Введите размер матрицы: "))
# for row in range(1, N + 1):
#     for col in range(1, N + 1):
#         if row % 2 == 0:
#             print(row, end="\t")
#         else:
#             print(col, end="\t")
#     print()




# N = int(input("Введите размер матрицы: "))
# for row in range(1, N + 1):
#     for col in range(1, N + 1):
#         if col % 3 == 0:
#             print(col, end="\t")
#         else:
#             print(row, end="\t")
#     print()



# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()



for row in range(20):
    for col in range(30):
        if row == 0:
            print("-", end="")
        elif col == 0 or col == 29:
            print("|", end="")
        else:
            print(" ", end="")
    print()



# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == row + 29:
#             print("\\", end="")
#         elif col == -row + 19:
#             print("/", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()


# N = int(input("Введите размер матрицы: "))
# for y in range(N):
#     for x in range(N):
#         buf_x = (N - 1) - y
#         if buf_x > x:
#             print(0, end='\t')
#         elif buf_x == x:
#             print(1, end='\t')
#         else:
#             print(2, end='\t')
#     print()



# n = int(input("Номер в очереди: "))

# for hour in range(n):
#     print("Часов прошло:", hour)
#     for num in range(hour, n):
#         print("Номер в очерди:", num)
#     print()
# print("Конец обслуживания")



# number = int(input("Введите число: "))
# new_nember = 0
# summ = 0
# while number > 0:
#     new_nember = number % 10
#     number //= 10
#     if new_nember > 5:
#         summ += 1
# print("Цифр больше 5:", summ)



# n = int(input("Введите число: "))
# for row in range(n + 1):
#     for col in range(row, n + 1):
#         print(col, end="\t")
#     print()