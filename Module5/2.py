numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("The greatest numbers in descending order:")
for number in numbers[:5]:
    print(number)
