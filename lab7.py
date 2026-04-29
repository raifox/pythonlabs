def save_and_print(filename, header, data):
    print(header.strip())
    with open(filename, 'w') as f:
        f.write(header)
        for line in data:
            print(line.strip())
            f.write(line)
    print("\n")

with open("african_crises.csv", 'r') as f:
    header = f.readline()
    lines = f.readlines()

cols = header.strip().split(',')
print("Доступні колонки:", cols, "\n")

# Завдання 1
col1 = input("Завдання 1. Введіть будь-яку колонку зі списку вище: ")
val1 = input("Введіть точне значення для пошуку: ")
idx1 = cols.index(col1)
res1 = [line for line in lines if line.strip().split(',')[idx1] == val1]
save_and_print("result_1.csv", header, res1)

# Завдання 2
col2 = input("Завдання 2. Введіть колонку з числами (напр. year, exch_usd, inflation_annual_cpi): ")
min_v = float(input("Мінімальне значення: "))
max_v = float(input("Максимальне значення: "))
idx2 = cols.index(col2)
res2 = []
for line in lines:
    try:
        if min_v <= float(line.strip().split(',')[idx2]) <= max_v:
            res2.append(line)
    except ValueError:
        pass
save_and_print("result_2.csv", header, res2)

# Завдання 3
col3 = input("Завдання 3. Введіть текстову колонку (напр. country, cc3): ")
letter = input("Введіть початкову літеру: ")
idx3 = cols.index(col3)
res3 = [line for line in lines if line.strip().split(',')[idx3].startswith(letter)]
save_and_print("result_3.csv", header, res3)

# Завдання 4
col4 = input("Завдання 4. Введіть текстову колонку (напр. country): ")
sub = input("Введіть підстрічку для пошуку: ")
idx4 = cols.index(col4)
res4 = [line for line in lines if sub in line.strip().split(',')[idx4]]
save_and_print("result_4.csv", header, res4)