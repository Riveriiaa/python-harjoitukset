gender= input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender != "male" and gender != "female":
    print("Invalid gender.")

if gender == "male":
    if hemoglobin< 134:
       print("Your hemoglobin is low.")
    elif hemoglobin> 167:
       print ("Your hemoglobin is high.")
    else:
       print ("Your hemoglobin is normal.")

elif gender == "female":
    if hemoglobin< 117:
       print ("Your hemoglobin is low.")
    elif hemoglobin>155:
       print ("Your hemoglobin is high.")
    else:
       print ("Your hemoglobin is normal.")