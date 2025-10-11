# reverse loop for loop
a = [1,2,3,4]
for i in reversed(a): # what does reversed function do the reson is it reverse the list 
    print(i)

# from user input reverse the number 
n = int(input("Enter a number to print reverse : "))
for i in range(n, 0,-1):
    print(i)