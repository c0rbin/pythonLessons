# --------------Циклы while------
# -------------------------------

# Простейший while
i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5: break

answer = None

while answer != 'Volvo':
    answer = input('Какая лучшая марка автомобиля? ')
print('Вы абсолютно правы!')

while i < 10:
    print(i)
    i = i + 1
    if i == 9: break
    if i < 3: continue
