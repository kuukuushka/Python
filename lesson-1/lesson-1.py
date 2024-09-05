name = input("Enter file:")  # Ввод имени файла
handle = open(name, 'r', encoding='utf-8')  # Открываем файл с указанием кодировки UTF-8
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1  # Считаем количество каждого слова

bigcount = None  # Инициализация переменной для хранения максимального количества повторений. Изначально она равна None.
bigword = None   # Инициализация переменной для хранения слова с наибольшим количеством повторений. Изначально она равна None.

# Цикл проходит по всем парам (слово, количество повторений) в словаре counts
for word, count in counts.items():
    
    # Если bigcount еще не инициализирован (на первой итерации) или если текущее слово встречается чаще, чем предыдущее "самое частое"
    if bigcount is None or count > bigcount:
        
        bigword = word   # Сохраняем текущее слово как самое частое
        bigcount = count # Сохраняем количество его повторений как максимальное на данный момент

print(bigword, bigcount)  # Выводим слово и количество его повторений



