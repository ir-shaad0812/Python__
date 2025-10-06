a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

# As we are going to ask input from user, we need to print the gratest between them 
if a >b :
    print("The greater number is ", a)
elif b > a:
    print("The greater number is ", b)
elif b == a:
    print("Both numbers are equal.")
else:
    print("Something went wrong..")
    
print("Thanks for using this code..")

