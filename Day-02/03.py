# Accept gender from user as char and print respective greetings message
gender = input("Please enter your gender (M/F): ")

if gender == "M" or gender == "m":
    print("Congratulations, Sir. You have been successfully registered as Male.")
elif gender == "F" or gender == "f":
    print("Congratulations, Madam. You have been successfully registered as Female.")
else:
    print("Invalid input. Please enter a valid gender (M or F).")

print("Thank you for participating in the survey.")
