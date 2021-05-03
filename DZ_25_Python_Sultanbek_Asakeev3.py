# Задание 3


spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
month_coeff = []
a = 0
for i in spendings:
    try:
        month_coeff.append(i / income[a])  #расход за месяц(i) / доход за месяц(a). проходит по каждому индексу 2х спсиков и при каждой итерации делит spending на income
    except ZeroDivisionError:
        month_coeff.append(0)  #Если выходит 0 то игнорируй(делай исключение и добавляй(append) 0), коээфициент этого месяца равняется 0
    a += 1
# print(month_coeff) #коэффициент для каждого месяца
month_sum = sum(month_coeff)  #суммируем коэффициенты за все месяцы с помощью sum(list)
# print(month_sum)
year_coefficient = month_sum / 12
print("Средний коэффициент распределения расходов за прошлый год: ",round(year_coefficient, 2))
