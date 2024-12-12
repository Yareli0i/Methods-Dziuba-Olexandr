import tkinter as tk
from tkinter import messagebox
import math

# Завдання 1: Точність наближень
def absolute_error(real_value, approx_value):
    return abs(real_value - approx_value)

def relative_error(real_value, approx_value):
    return absolute_error(real_value, approx_value) / real_value

def task1():
    try:
        sqrt_n1_real = 9.11  # Справжнє значення sqrt(83)
        x1 = float(entry_x1.get())
        exact_ratio = 6 / 11  # Справжнє значення 6/11
        x2 = float(entry_x2.get())

        rel_error1 = relative_error(sqrt_n1_real, x1)
        rel_error2 = relative_error(exact_ratio, x2)

        if rel_error1 < rel_error2:
            result_task1.set(f"Наближення до sqrt(83) точніше: відносна похибка = {rel_error1:.4f}")
        else:
            result_task1.set(f"Наближення до 6/11 точніше: відносна похибка = {rel_error2:.4f}")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")

# Завдання 2: Округлення числа
def round_narrow(x, delta):
    return round(x, 2) if delta < 0.05 else round(x, 1)

def round_broad(x, delta_percent):
    delta = delta_percent / 100
    return round(x, 2) if delta < 0.05 else round(x, 1)

def task2():
    try:
        rounding_choice = rounding_mode.get()

        if rounding_choice == 'narrow':
            x = 3.7834
            delta = 0.0041
            x_narrow = round_narrow(x, delta)
            result_task2.set(f"Округлене число (вузьке) = {x_narrow}")
        elif rounding_choice == 'broad':
            x = 21.68563
            delta_percent = 0.3
            x_broad = round_broad(x, delta_percent)
            result_task2.set(f"Округлене число (широке) = {x_broad}")
        else:
            messagebox.showerror("Помилка", "Оберіть режим округлення.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")

# Завдання 3: Обчислення похибок
def calculate_delta_narrow(x):
    try:
        decimal_places = len(str(x).split(".")[1]) if "." in str(x) else 0
        last_digit_value = 10 ** (-decimal_places)
        return last_digit_value / 2
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка обчислення вузької похибки: {str(e)}")
        return None

def calculate_delta_broad(x):
    try:
        decimal_places = len(str(x).split(".")[1]) if "." in str(x) else 0
        last_digit_value = 10 ** (-decimal_places)
        return last_digit_value
    except Exception as e:
        messagebox.showerror("Помилка", f"Помилка обчислення широкої похибки: {str(e)}")
        return None

def task3():
    try:
        choice = error_mode.get()

        if choice == 'narrow':
            x = 41.72
            delta_narrow = calculate_delta_narrow(x)
            if delta_narrow is not None:
                relative_error = delta_narrow / x
                result_task3.set(f"Абсолютна похибка (вузьке) = {delta_narrow:.4f}, Відносна похибка = {relative_error * 100:.4f}%")
            else:
                result_task3.set("Не вдалося обчислити похибку.")
        elif choice == 'broad':
            x = 0.678
            delta_broad = calculate_delta_broad(x)
            if delta_broad is not None:
                relative_error = delta_broad / x
                result_task3.set(f"Абсолютна похибка (широке) = {delta_broad:.4f}, Відносна похибка = {relative_error * 100:.4f}%")
            else:
                result_task3.set("Не вдалося обчислити похибку.")
        else:
            messagebox.showerror("Помилка", "Оберіть тип похибки.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")

def main():
    global entry_x1, entry_x2
    global rounding_mode
    global error_mode
    global result_task1, result_task2, result_task3

    root = tk.Tk()
    root.title("Три завдання: Точність, Округлення та Похибки")
    root.geometry("400x500")

    tk.Label(root, text="Завдання 1: Точність наближень", font=("Arial", 10, "bold")).pack(pady=5)

    tk.Label(root, text="Наближення sqrt(83):").pack()
    entry_x1 = tk.Entry(root)
    entry_x1.pack()

    tk.Label(root, text="Наближення 6/11:").pack()
    entry_x2 = tk.Entry(root)
    entry_x2.pack()

    result_task1 = tk.StringVar()
    tk.Button(root, text="Виконати завдання 1", command=task1).pack(pady=5)
    tk.Label(root, textvariable=result_task1).pack(pady=5)

    tk.Label(root, text="Завдання 2: Округлення числа", font=("Arial", 10, "bold")).pack(pady=5)

    rounding_mode = tk.StringVar(value='narrow')
    tk.Radiobutton(root, text="Вузьке", variable=rounding_mode, value='narrow').pack()
    tk.Radiobutton(root, text="Широке", variable=rounding_mode, value='broad').pack()

    result_task2 = tk.StringVar()
    tk.Button(root, text="Виконати завдання 2", command=task2).pack(pady=5)
    tk.Label(root, textvariable=result_task2).pack(pady=5)

    tk.Label(root, text="Завдання 3: Обчислення похибок", font=("Arial", 10, "bold")).pack(pady=5)

    error_mode = tk.StringVar(value='narrow')
    tk.Radiobutton(root, text="Вузьке", variable=error_mode, value='narrow').pack()
    tk.Radiobutton(root, text="Широке", variable=error_mode, value='broad').pack()

    result_task3 = tk.StringVar()
    tk.Button(root, text="Виконати завдання 3", command=task3).pack(pady=5)
    tk.Label(root, textvariable=result_task3).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
