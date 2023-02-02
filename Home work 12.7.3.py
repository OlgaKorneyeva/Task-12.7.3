# Процентные ставки по вкладам в различных банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# Суммы, которые планируется положить под процентны
money = int(input("Введите сумму, которую планируете внести: "))
# Создание списка процентных ставок в банках
percent = list(per_cent.values()) 
print(list(percent))
# Выводим доход в каждом банке
bankTKB = money*percent[0]/100
bankCKB = money*percent[1]/100 
bankBTБ = money*percent[2]/100
bankСБЕР = money*percent[3]/100
# Накопленные средства за год вклада в каждом банке
deposit = [bankTKB, bankCKB, bankBTБ, bankСБЕР]
print("deposit =", deposit)
# Вывод максимальной суммы
print("Максимальная сумма, которую вы можете заработать -", max(deposit))