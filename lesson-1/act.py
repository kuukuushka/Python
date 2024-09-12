# # Калькулятор 

# num_1 = int(input("Удаленная техническая поддержка пользователей: "))
# num_2 = int(input("Мониторинг узлов сети: "))
# num_3 = int(input("Удаленная настройка сетевого оборудования (Linksys SPS 224G4): "))
# num_4 = int(input("Удаленная настройка сетевого оборудования (D-Link DES-3526): "))
# num_5 = int(input("Удаленная настройка сетевого оборудования (Cisco SF300-24): "))
# num_6 = int(input("Удаленная настройка сетевого оборудования (Eltex MES1124): "))
# num_7 = int(input("Удаленная настройка сетевого оборудования (Eltex MES2324FB): "))
# num_8 = int(input("Диагностика и устранение внештатных проблем оборудования: "))

# summ = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8
# print(summ)



# total_amount = int(input("Введи итоговую сумму: "))

# # Час работы
# time_1 = 311
# opening_hours_1 = 0
# time_2 = 330
# opening_hours_2 = 0
# time_3 = 480 
# opening_hours_2 = 0

# # Настройка оборудывания 
# product_1 = 1200
# product_2 = 1000
# product_3 = 1500 
# product_4 = 1100 
# product_5 = 3000

# # Сумма 
# summ = 0



# Ввод итоговой суммы
total_amount = int(input("Введи итоговую сумму: "))

# Час работы для разных типов услуг
support_price = 311  # Удаленная техническая поддержка пользователей
monitoring_price = 330  # Мониторинг узлов сети
diagnostics_price = 480  # Диагностика и устранение внештатных проблем оборудования (максимум 10 часов)

# Стоимость продуктов (настройка оборудования)
product_1_price = 1200
product_2_price = 1000
product_3_price = 1500
product_4_price = 1100
product_5_price = 3000

# Лимиты на количество часов и количество продуктов
max_hours = 30  # Максимальное количество часов для каждой категории работы
max_diagnostics_hours = 10  # Максимум 10 часов для диагностики
max_products = 5  # Максимальное количество для каждого продукта

# Рассчитываем минимальную и максимальную возможную сумму для работы
min_work_sum = (1 * support_price) + (1 * monitoring_price) + (1 * diagnostics_price)
max_work_sum = (max_hours * support_price) + (max_hours * monitoring_price) + (max_diagnostics_hours * diagnostics_price)

# Если сумма вне диапазона работы + продукты, выводим сообщение и выходим
if total_amount < min_work_sum or total_amount > max_work_sum + (product_1_price * max_products) + (product_2_price * max_products) + \
   (product_3_price * max_products) + (product_4_price * max_products) + (product_5_price * max_products):
    print("Не удается подобрать комбинацию для данной суммы.")
else:
    # Поиск подходящих значений времени работы и количества продуктов
    for support_hours in range(1, max_hours + 1):  # Удаленная техподдержка
        for monitoring_hours in range(1, max_hours + 1):  # Мониторинг узлов
            for diagnostics_hours in range(1, min(max_diagnostics_hours, support_hours, monitoring_hours) + 1):  # Диагностика
                # Считаем сумму работы
                total_work_sum = (support_hours * support_price) + (monitoring_hours * monitoring_price) + (diagnostics_hours * diagnostics_price)

                # Оставшаяся сумма на продукты
                remaining_sum = total_amount - total_work_sum

                # Перебор возможных комбинаций продуктов
                for product_1_count in range(0, max_products + 1):
                    for product_2_count in range(0, max_products + 1):
                        for product_3_count in range(0, max_products + 1):
                            for product_4_count in range(0, max_products + 1):
                                for product_5_count in range(0, max_products + 1):
                                    # Сумма стоимости всех продуктов
                                    total_product_sum = (
                                        product_1_count * product_1_price +
                                        product_2_count * product_2_price +
                                        product_3_count * product_3_price +
                                        product_4_count * product_4_price +
                                        product_5_count * product_5_price
                                    )

                                    # Если сумма продуктов равна оставшейся сумме
                                    if total_product_sum == remaining_sum:
                                        print(f"Часы работы:")
                                        print(f"  - Удаленная техподдержка: {support_hours} ч.")
                                        print(f"  - Мониторинг узлов: {monitoring_hours} ч.")
                                        print(f"  - Диагностика и устранение: {diagnostics_hours} ч. (макс. 10 ч.)")

                                        print("\nПродукты:")
                                        print(f"  - Linksys SPS 224G4: {product_1_count} шт. x {product_1_price} руб. = {product_1_count * product_1_price} руб.")
                                        print(f"  - D-Link DES-3526: {product_2_count} шт. x {product_2_price} руб. = {product_2_count * product_2_price} руб.")
                                        print(f"  - Cisco SF300-24: {product_3_count} шт. x {product_3_price} руб. = {product_3_count * product_3_price} руб.")
                                        print(f"  - Eltex MES1124: {product_4_count} шт. x {product_4_price} руб. = {product_4_count * product_4_price} руб.")
                                        print(f"  - Eltex MES2324FB: {product_5_count} шт. x {product_5_price} руб. = {product_5_count * product_5_price} руб.")
                                        
                                        # Вывод общей суммы за продукты
                                        print(f"\nОбщая сумма за продукты: {total_product_sum} руб.")
                                        
                                        # Вывод итоговой суммы (работа + продукты)
                                        print(f"\nИтоговая сумма для всех работ и продуктов: {total_amount} руб.")
                                        exit()

print("Не удалось подобрать время работы и количество продуктов для данной суммы.")









