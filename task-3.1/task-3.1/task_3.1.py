lst = []
x = 1
while x != 0:
    x = float(input("Зарплата сотрудников:"))
    if x != 0:
        lst.append(x)
if len(lst) > 0:
    sr_x = sum(lst) / len(lst)
    print("Средняя зарплата сотрудников: ", sr_x)
else:
    print("Список пуст")


