import pandas as pd
import numpy as np

print("--- Зчитування даних з csv-файлу у DataFrame ---")
df = pd.read_csv('african_crises.csv')
print(df.head())

print("\n--- Фільтрування даних за критеріями ---")
filtered_exact = df[df['year'] == 2000]
print(filtered_exact.head())

filtered_range = df[df['year'].between(1990, 2000)]
print(filtered_range.head())

start_char = input("Введіть першу літеру для пошуку по країні: ")
filtered_starts = df[df['country'].str.startswith(start_char, na=False)]
print(filtered_starts.head())

substring = input("Введіть підстрічку для пошуку по країні: ")
filtered_contains = df[df['country'].str.contains(substring, na=False)]
print(filtered_contains.head())

print("\n--- Сортування даних за критеріями ---")
sorted_asc_one = df.sort_values(by='inflation_annual_cpi', ascending=True)
sorted_desc_one = df.sort_values(by='inflation_annual_cpi', ascending=False)

sorted_two_cols = df.sort_values(by=['country', 'year'], ascending=[True, False])
print(sorted_two_cols.head())

print("\n--- Групування даних по певному полі ---")
grouped_stats = df.groupby('country')['inflation_annual_cpi'].agg(['min', 'max', 'mean', 'std']).reset_index()
print(grouped_stats)

print("\n--- Створення додаткового датасету та об’єднання ---")
unique_countries = df['country'].unique()
additional_df = pd.DataFrame({
    'country': unique_countries,
    'Test Column': np.random.randint(100, 999, size=len(unique_countries))
})

merged_df = pd.merge(df, additional_df, on='country', how='left')
print(merged_df.head())