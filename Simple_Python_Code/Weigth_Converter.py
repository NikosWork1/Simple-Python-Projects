weight=float(input("Enter your weight: "))
units=input("Kilograms or Pounds? (K or L): ")
if units=="K":
    weight=weight*2.205
    units="lbs"
    print(f"Your weight is : {weight}{units}")
elif units=="L":
    weight=weight/2.205
    units="Kgs"
    print(f"Your weight is : {weight}4566{units}")
else:
    print(f"{units} is not a valid unit.\nPlease select a valid input.(K or L)")
