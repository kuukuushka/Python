# positive = 0
# for i in range(10):
#     number = int(input("Введите число: "))
#     if (number % 2 == 0) and (number > 0):
#         positive += 1
# print("Чётными и положительные:", positive)



# total_date = 0
# summ = 0
# for i in range(12):
#     total_date += 1
#     money = int(input("Введите свою зарплату за месяц: "))
#     summ += money
# summ /= 12
# print(summ)


number = int(input("Введите число: "))
summ = 1
for i in range(2, number + 1):
    summ *= i
print(summ)




