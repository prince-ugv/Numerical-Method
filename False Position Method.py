import math

# Function definition
def f(x):
    return 3 * x - math.cos(x) - 1

# Input initial values
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

# Tolerance and maximum iterations
tolerance = 1e-6
max_iterations = 50

# Check if initial values are valid
if f(a) * f(b) > 0:
    print("\nInvalid initial values! f(a) * f(b) > 0 — No sign change.")
    print("Please choose different values of a and b.")
else:
    print("\nIteration\t   a\t\t   b\t\t   c\t\t  f(c)")
    for i in range(1, max_iterations + 1):
        fa = f(a)
        fb = f(b)

        # False position formula
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        # Show current step
        print(f"{i:>5}\t{a:10.6f}\t{b:10.6f}\t{c:10.6f}\t{fc:10.6f}")

        # Check for convergence
        if abs(fc) < tolerance:
            print(f"\nApproximate root found (tolerance met) = {c:.6f}")
            break

        # Update interval based on sign
        if fa * fc < 0:
            b = c
        else:
            a = c
    else:
        print("\nStopped: Maximum number of iterations reached.")
        print(f"Last approximation of root = {c:.6f}")
