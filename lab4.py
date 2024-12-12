import math
import pandas as pd
import matplotlib.pyplot as plt


def get_function(default_func_description, default_func):
    return default_func


def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(n)) * h
    return result


def simpsons_method(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    h = (b - a) / n
    s1 = sum(f(a + i * h) for i in range(1, n, 2))
    s2 = sum(f(a + i * h) for i in range(2, n, 2))
    return h / 3 * (f(a) + f(b) + 4 * s1 + 2 * s2)


def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    s = sum(f(a + i * h) for i in range(1, n))
    s += (f(a) + f(b)) / 2
    return s * h


def generate_xy_table(f, a, b, n):
    h = (b - a) / n
    data = {
        "i": range(n + 1),
        "x_i": [round(a + i * h, 4) for i in range(n + 1)],
        "y_i": [round(f(a + i * h), 4) for i in range(n + 1)]
    }
    return pd.DataFrame(data)


def main():
    tasks = {
        "1": ("∫(0.4 to 1.2) (dx / sqrt(x + 3))", lambda x: 1 / math.sqrt(x + 3), 0.4, 1.2, "Rectangle", 10),
        "2": ("∫(0.4 to 1.2) ((2x + 0.5) * sin x dx)", lambda x: (2 * x + 0.5) * math.sin(x), 0.4, 1.2, "Simpson's", 8),
        "3": (
        "∫(1.2 to 2) (dx / sqrt(0.5x^2 + 1.5))", lambda x: 1 / math.sqrt(0.5 * x ** 2 + 1.5), 1.2, 2.0, "Trapezoidal",
        20)
    }

    for task, (desc, f, a, b, method_name, n) in tasks.items():
        print(f"Task {task}: {desc}")

        if method_name == "Rectangle":
            result = rectangle_method(f, a, b, n)
        elif method_name == "Simpson's":
            result = simpsons_method(f, a, b, n)
        elif method_name == "Trapezoidal":
            result = trapezoidal_method(f, a, b, n)
        else:
            print("Invalid method")
            continue

        xy_table_df = generate_xy_table(f, a, b, n)
        print("\nTable of x_i and y_i values:")
        print(xy_table_df.to_string(index=False))

        print(f"\nIntegration result using {method_name} method with n={n}: {result:.4f}\n")

        plt.figure(figsize=(10, 5))
        plt.plot(xy_table_df["x_i"], xy_table_df["y_i"], marker="o", linestyle="-", label=f"Function f(x)")
        plt.title(f"Function values f(x) for {method_name} Method - Task {task}")
        plt.xlabel("x_i")
        plt.ylabel("y_i")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
