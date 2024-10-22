numbers=[152,15102,1500164521,4189431321,5,56465123694,231416540,651,546,4754546]
min_number=numbers[0]
for num in numbers:
    if num<min_number:
        min_number=num
print(f"The min number is {min_number}")