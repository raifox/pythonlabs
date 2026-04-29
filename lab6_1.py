import math

def calc_a(x, y, z, b):
    num = abs(x**2 - x)**31.5 - 3 * (abs(y + 2*b)**(1/3))
    den = 1 + x + (y**2 / 2) + (x**3 / 6)
    if den == 0:
        raise ZeroDivisionError("Знаменник у calc_a дорівнює нулю при поточних значеннях x та y.")
    return num / den

def calc_b(x, y, z):
    if y == 0:
        raise ZeroDivisionError("Значення y не може дорівнювати 0, оскільки відбувається ділення на y у calc_b.")
    return x * (((y + math.atan(abs(x**2 + z)**0.1)) / (3 + math.sin(y**3)**2)) + math.exp((x + z) / y))

if __name__ == "__main__":
    print("--- Завдання 1.1 ---")
    x = float(input("Введіть значення x: "))
    y = float(input("Введіть значення y: "))
    z = float(input("Введіть значення z: "))
    b = float(input("Введіть значення b: "))
    
    print(f"Результат функції a: {calc_a(x, y, z, b)}")
    print(f"Результат функції b: {calc_b(x, y, z)}")