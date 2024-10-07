# text_sum = 0
# for i in range(10):
#     text = input("Введите текст: ")
#     if text == "Карамба" or text == "карамба":
#         text_sum += 1
# print("Попали в команду:", text_sum)



# text = input("Введите текст: ")
# for index, symbol in enumerate(text, start=1):
#     if symbol == "*":
#         print("Символ", symbol, "находится на", index, "позиции в тексте")



# rows = int(input("Введите кол-во рядов: "))
# seats = int(input("Введите кол-во сидений в ряде: "))
# meters = int(input("Введите кол-во метров между рядами: "))

# print("\nСцена\n")

# for i in range(rows):
#     for i in range(seats):
#         print("=", end="")
#         if i == seats - 1:
#             print(end=" ")
#     for i in range(meters):
#         print("*", end="")
#     for i in range(seats):
#         if i == 0:
#             print(end=" ")
#         print("=", end="")
#     print()

# for row in range(rows):
#     print("=" * seats + " " + "*" * meters + " " + "=" * seats)



# start_x = 6
# start_y = 19

# while True:
#     print("[Программа]: Марсоход находится на позиции", start_x, start_y, "введите команду:")
#     step = input("[Оператор]: ")
#     if step == "W" and start_y < 20:
#             start_y += 1
#     elif step == "S" and 1 < start_y:
#             start_y -= 1
#     elif step == "D" and start_x < 15:
#             start_x += 1
#     elif step == "A" and 1 < start_x:
#             start_x -= 1



# text = input("Введите текст: ")
# max_word_length = 0  # Длина самого длинного слова
# current_word_length = 0  # Длина текущего слова

# for char in text:
#     if char != " " and char != ".":  # Если это не пробел или точка, увеличиваем длину текущего слова
#         current_word_length += 1
#     else:
#         # Если встречаем пробел или точку, сравниваем длину текущего слова с максимальной
#         if current_word_length > max_word_length:
#             max_word_length = current_word_length
#         current_word_length = 0  # Сбрасываем длину текущего слова

# # Проверка последнего слова (если текст не заканчивается пробелом или точкой)
# if current_word_length > max_word_length:
#     max_word_length = current_word_length

# print(f"Самое длинное слово, букв: {max_word_length}")


    


# racks = input("Какие стойки заняты ?")
# summ = 0
# if len(racks) == 10:
#     for index, i in enumerate(racks):
#         milk = (index + 1) * 2 
#         if i == "b":
#             summ += milk
#     print("Всего молока:", summ)
# else: 
#     print("Чисел не 10")




# # Ввод зашифрованного сообщения
# encrypted_message = input("Введите зашифрованное сообщение: ")

# # Длина зашифрованного сообщения
# length = len(encrypted_message)

# # Инициализация списка для расшифрованного сообщения
# decrypted_message = [''] * length

# # Заполняем расшифрованное сообщение
# for i in range(length):
#     if i % 2 == 0:  # Нечётные индексы (1, 3, 5...)
#         decrypted_message[i // 2] = encrypted_message[i]
#     else:  # Чётные индексы (2, 4, 6...)
#         decrypted_message[length - (i // 2) - 1] = encrypted_message[i]

# # Преобразуем список в строку
# decrypted_message = ''.join(decrypted_message)

# # Вывод расшифрованного сообщения
# print("Расшифрованное сообщение:", decrypted_message)

    



# Ввод строки от пользователя
original_message = input("Введите фрагмент послания: ")

# Убираем пробелы и приводим к нижнему регистру
cleaned_message = original_message.replace(" ", "").lower()

# Инициализируем переменную для развернутой строки
reversed_message = ""

# Проходим по каждому символу в строке и строим развернутую строку
for char in cleaned_message:
    reversed_message = char + reversed_message  # Добавляем символ в начало
    print(reversed_message)

# Сравниваем оригинальное сообщение с развернутым
if cleaned_message == reversed_message:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")
