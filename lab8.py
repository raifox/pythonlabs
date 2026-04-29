import numpy as np
import csv

data = np.genfromtxt('african_crises.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')

# Завдання 1
sort_1_asc = np.sort(data, order='year')
sort_1_desc = np.sort(data, order='year')[::-1]

# Завдання 2
sort_2_asc = np.sort(data, order=['country', 'year'])
sort_2_desc = np.sort(data, order=['country', 'year'])[::-1]

# Завдання 3: Виведення результатів та запис у файли
def save_and_show(dataset, filename, start=0, end=None):
    subset = dataset[start:end] if end else dataset[start:]
    print(subset)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(dataset.dtype.names)
        for row in subset:
            writer.writerow(row)

save_and_show(sort_1_asc, 'sort_1_asc.csv', 0, 5)
save_and_show(sort_1_desc, 'sort_1_desc.csv', 0, 5)
save_and_show(sort_2_asc, 'sort_2_asc.csv', 0, 5)
save_and_show(sort_2_desc, 'sort_2_desc.csv')