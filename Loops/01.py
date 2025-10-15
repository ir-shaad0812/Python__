# Loop 10 times 1 to 10
# for i in range(1, 11, 2):
#     print(i)
    # let's print a  table of 13

# loops for table of any number from user input
num = int (input("Enter a number to print its table: "))
for i in range (num, (num*10)+1, num):
    print(i)