# Leap Year or not and also show the next 10 leap years and remaining years to next leap year

year = int(input("Please enter the year: "))

if year % 100 == 0 or year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 != 0 and year % 4== 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
