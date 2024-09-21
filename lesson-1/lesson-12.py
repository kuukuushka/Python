# n = int(input("Введите число: "))
# summ = 0
# for i in range(1, n//2 + 1):
#     i *= 2
#     print(i, "** 3 = ", i ** 3)



total_time = int(input("Количество часов: "))
cell = 1
for time in range(1, total_time // 3 + 1):
    cell *= 2

    print("Прошло часов:", time * 3)
    print("Количество клеток:", cell)
    print("Осталось часов:", total_time - time * 3 )
    print()
print("Конец")


