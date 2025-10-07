#  Check the user is valid for vote  or not and also  view the remaining years to vote
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(f"\nHello, {name}!")

if age < 18:
    years_left = 18 - age
    print("Sorry, you are not eligible to vote yet.")
    print(f"You will be eligible to vote in {years_left} year(s).")
elif age >= 18:
    print("Congratulations! You are eligible to vote.")
else:
    print("Not valid.")
