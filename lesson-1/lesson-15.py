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


    


    


        




