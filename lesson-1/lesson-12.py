n = int(input("Введите число: "))
summ = 0
for i in range(1, n//2 + 1):
    i *= 2
    print(i, "** 3 = ", i ** 3)



# total_time = int(input("Количество часов: "))
# cell = 1
# for time in range(1, total_time // 3 + 1):
#     cell *= 2

#     print("Прошло часов:", time * 3)
#     print("Количество клеток:", cell)
#     print("Осталось часов:", total_time - time * 3 )
#     print()
# print("Конец")



# n = int(input("Введите число: "))
# summ = 0
# for i in range(1, n//2 + n%2 + 1):
#     i = i * 2 - 1
#     print(i, "** 2 =", i ** 2)
    

    


# n = int(input("Введите число: "))
# number = 1
# summ = 0
# while (n >= number):
#     summ = number ** 2
#     print(number, "** 2 =", summ)
#     number += 2
    



# number = int(input("Введите число: "))
# for i in range(1, number, 2):
#     print(i, "** 3 =", i ** 3)



# number = int(input("Введите число: "))
# summ = 0 
# for i in range(1, number + 1, 5):
#     print("Номер стула", i)
#     summ += i
# print("Сумма: ", summ)



wake_up = int(input("Во сколько встал: "))
water = 0
calories_summ = 0

for time in range(wake_up, 23, 3):
    print("Сейчас:", time)
    print("Выпил воды 3 литра")
    calories = int(input("Сколько съел калорий ? "))
    calories_summ += calories
    water += 3
    
print("Всего калорий:", calories_summ)
print("Выпил воды:", water)

    

