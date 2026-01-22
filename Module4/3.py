numbers = []


while True:
    s = input("Enter a number (or press Enter to quit):")
    if s == "":
       break
    numbers.append(float(s))

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")

