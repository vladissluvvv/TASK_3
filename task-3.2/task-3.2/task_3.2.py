num = input()
x = {}
for i in range(10):
    x[str(i)] = 0
for n in num:
    x[n] += 1
    print(x)
for k, v in x.items():
    print(k + " - " + str(v))
