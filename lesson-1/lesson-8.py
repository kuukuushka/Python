# number_of_lines = int(input("Введите количество строк: "))
# link = 0
# while link < number_of_lines:
#     print("Я — программист!")
#     link += 1



# number = int(input("Сколько раз напомнить: "))
# summ_link = 0
# while summ_link < number:
#     print("Вы хотели не забыть о чём-то")
#     summ_link += 1



bag = int(input("Сколько мешков: "))
total_bag = 0
weight_bag = 0 
summ_bag = 0
while total_bag < bag:
    weight_bag = int(input("Сколько весит мешок: "))  # weight_bag += int(input("Сколько весит мешок: "))
    total_bag += 1
    summ_bag += weight_bag
print("Вес всех мешков:", summ_bag)

