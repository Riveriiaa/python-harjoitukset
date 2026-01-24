import random

N = int(input().strip())

inside = 0
i = 0

while i < N:
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x * x + y * y < 1.0:
        inside += 1

    i += 1

pi_approx = 4.0 * inside / N
print(f"Approximation of pi: {pi_approx}")

