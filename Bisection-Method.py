import math

def f(x):
    return 3 * x - math.cos(x) - 1

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

max_iterations = 50
tolerance = 1e-3

if f(a) * f(b) > 0:
    print("\nInvalid initial values! f(a) * f(b) > 0 — No sign change.")
    print("Please choose different values of a and b.")
else:
    print("\nIteration\t   a\t\t   b\t\t   c\t\t  f(a)\t\t  f(b)\t\t  f(c)")
    i = 1
    while i <= max_iterations:
        c = (a + b) / 2
        fa, fb, fc = f(a), f(b), f(c)
        print(f"{i:>5}\t{a:10.6f}\t{b:10.6f}\t{c:10.6f}\t{fa:10.6f}\t{fb:10.6f}\t{fc:10.6f}")

        if abs(fc) < tolerance:
            print(f"\nApproximate root found (tolerance met) = {c:.6f}")
            break

        if fa * fc < 0:
            b = c
        else:
            a = c
        i += 1

    if i > max_iterations:
        print("\nStopped: Maximum number of iterations reached.")
        print(f"Last approximation of root = {c:.6f}")
