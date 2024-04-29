s = input("")
w = s.split()
long_w = max(w, key = len)
print("Самое длинное слово в этом предложении: ", long_w)
