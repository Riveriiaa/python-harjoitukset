def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return "winter"
    elif month >= 3 and month <= 5:
        return "spring"
    elif month >= 6 and month <= 8:
        return "summer"
    elif month >= 9 and month <= 11:
        return "autumn"
    else:
        return None


month = int(input("Enter the number of a month (1-12): "))
print(f"You entered: {month}")

season = get_season(month)

if season is None:
    print("Please enter a number between 1 and 12.")
else:
    print(f"The season is {season}.")