import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def lagrange_interpolation(XX, YY):
    x = sp.Symbol('x')
    n = len(XX)
    L = 0
    for i in range(n):
        term = YY[i]
        for j in range(n):
            if i != j:
                term *= (x - XX[j]) / (XX[i] - XX[j])
        L += term
    return sp.simplify(L)

def task_variant_9():
    XX = [-2, 0, 1, 2]
    YY = [30, -4, 3, 18]
    points_to_interpolate = [-1.5, -1, -0.5, 1.5]

    # Виведення таблиці значень
    table = "\nTable of values of a function:\n"
    table += "X: " + "".join([f"{x:7.3f}|" for x in XX]) + "\n"
    table += "Y: " + "".join([f"{y:7.3f}|" for y in YY]) + "\n"
    print(table)
    messagebox.showinfo("Values Table", table)

    # Обчислення інтерполяційного багаточлена
    L_simplified = lagrange_interpolation(XX, YY)

    # Виведення інтерполяційного багаточлена
    result = f"The interpolation polynomial L(x) is:\n{L_simplified}\n"
    print(result)
    messagebox.showinfo("Lagrange Polynomial", result)

    # Інтерполяція заданих точок
    interpolation_results = ""
    for r in points_to_interpolate:
        y_value = L_simplified.subs(sp.Symbol('x'), r)
        interpolation_results += f"For X = {r:.1f}, Y = {y_value:.3f}\n"
    print(interpolation_results)
    messagebox.showinfo("Interpolation Results", interpolation_results)

    # Побудова графіка
    plot_graph(XX, YY, L_simplified, points_to_interpolate)

def plot_graph(XX, YY, L_simplified, points_to_interpolate):
    L_func = sp.lambdify(sp.Symbol('x'), L_simplified, 'numpy')
    x_vals = np.linspace(min(XX) - 1, max(XX) + 1, 500)
    y_vals = L_func(x_vals)

    # Побудова графіка
    plt.plot(x_vals, y_vals, label='Lagrange Polynomial', color='orange')
    plt.scatter(XX, YY, color='blue', label='Given Points')

    for r in points_to_interpolate:
        plt.scatter(r, L_func(r), color='red')

    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')

    plt.title('Lagrange Interpolation Polynomial')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    root = tk.Tk()
    root.title("Lagrange Interpolation Variant 9")

    tk.Button(root, text="Run Variant 9", command=task_variant_9).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
