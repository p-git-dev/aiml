def f(x):
    return 25 - (x - 5) ** 2


def hill_climb(x, step=0.01, limit=2000):
    for _ in range(limit):
        left, right = max(-10, x - step), min(10, x + step)
        best = max((left, right), key=f)
        if f(best) <= f(x):
            break
        x = best
    return x


if __name__ == "__main__":
    try:
        x = float(input("Starting x [-10, 10] (Enter for 0): ").strip() or 0)
    except ValueError:
        raise SystemExit("Enter a number between -10 and 10.")
    if not -10 <= x <= 10:
        raise SystemExit("Enter a number between -10 and 10.")
    x = hill_climb(x)
    print(f"x = {x:.4f}\nf(x) = {f(x):.4f}")
