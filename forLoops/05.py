# # Print sum of two numberr
# a = int(input("Enter first number : "))
# sum = 0

# for i in range(1,11): # print sum of first 10 natural number
#     sum = sum + i
# print(f"The sum of first 10 natural number is : {sum}")


# Print sum of n number from user input
n = int(input("Enter a number to print sum of natural numbers : "))
sum = 0

for i in range(1,n+1):
    sum += i 
print(f"The sum of natural numbers up to {n} is : {sum}")