kuha= float(input("Enter the length of the zander in centimeters: "))

if kuha < 42:
    s = round(42 - kuha, 1)
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {s} centimeters below the size limit.")

else:
    print("The zander meets the size limit.")