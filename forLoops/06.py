#  Factorial of a number using for loop
n = int(input("Enter a number to find factorial : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"Factorial of {n} is : {fact}")