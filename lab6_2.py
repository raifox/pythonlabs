def root(f, a, b, eps):
    mid = (a + b) / 2.0
    if (b - a) / 2.0 < eps:
        return mid
    return root(f, a, mid, eps) if f(a) * f(mid) < 0 else root(f, mid, b, eps)

if __name__ == "__main__":
    print("--- Завдання 2.1 ---")
    print("Шукаємо корінь для рівняння: x^2 - 4 = 0")
    
    a = float(input("Введіть початок відрізка a (наприклад, 0, де значення функції від'ємне): "))
    b = float(input("Введіть кінець відрізка b (наприклад, 5, де значення функції додатне): "))
    eps = float(input("Введіть точність eps (наприклад, 0.001 — чим менше значення, тим вища точність): "))
    
    func = lambda x: x**2 - 4
    
    if func(a) * func(b) >= 0:
        print("Помилка: Значення функції на кінцях відрізка мають бути різних знаків.")
    else:
        print(f"Знайдений корінь: {root(func, a, b, eps)}")