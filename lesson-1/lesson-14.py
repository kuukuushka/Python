# total_poor_rating = 0

# for student in range(5):
#     answer = input("Кто написал произведение? ")
#     if (answer == "Пушкин") or (answer == "пушкин"):
#         print("Конец")
#         break
#     print("Двойка")
#     total_poor_rating += 1
# print("Всего довек:", total_poor_rating)



# while True:
#     home_work = input("Выполнил ли ты задание, которое выдавал вчера ? ")
#     if (home_work == "Да") or (home_work == "да"):
#         print("Молодец")
#         break
    



# name = input("Как тебя зовут ? ")
# print(name + ", купи слона!")
# while True:
#     answer = input()
#     print("Всегда говорят", answer + ", давай куплю, а ты купи слона!")



# text = "Enumerate в Python"
# for index, symbol in enumerate(text):
#     print("Символ", symbol, "находится на", index, "позиции в тексте")
# # Чтобы считать символы в привычном нам формате, 
# # начиная с единицы можно использовать параметр start
# for index, symbol in enumerate(text, start=1):
#     print("Символ", symbol, "находится на", index, "позиции в тексте")



# text = "Python"
# for i in text:
#     print(i)


# text = input("Введите текст:")
# for i in text:
#     print(i * 3)




# text = input("Введите текст: ")
# big_text = 0 
# little_text = 0

# for i in text:
#     if i == "Ы":
#         big_text += 1
#     elif i == "ы":
#         little_text += 1
# print("Больших букв Ы:", big_text)
# print("Маленьких букв Ы:", little_text)



text = "0"

for i in range(10):
    print(text, end="")