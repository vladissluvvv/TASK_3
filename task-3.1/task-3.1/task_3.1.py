lst = []
x = 1
while x != 0:
    x = float(input("�������� �����������:"))
    if x != 0:
        lst.append(x)
if len(lst) > 0:
    sr_x = sum(lst) / len(lst)
    print("������� �������� �����������: ", sr_x)
else:
    print("������ ����")


