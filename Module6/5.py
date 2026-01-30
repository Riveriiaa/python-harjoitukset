def filter_even_numbers(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(number_list)

print("Original list:", number_list)
print("List with even numbers only:", filtered_list)
