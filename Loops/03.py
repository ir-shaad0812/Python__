# # break loop

for i in range (1, 21):
    if i == 10:
        continue # skip the value 10 as continue will skip value of 10 and continue to next value
    elif i == 15:
        break # break the loop when value 20 is reached
    print(i)

# break loop works with else statement ..When break works then else will not run and vice-versa
# For eg:
for i in range (1, 11):
    if i ==5: # when i value is 5 then break will execute and else will not execute
        print("Break executed")
        break
    print(i)
else: #when  i value  will be more than range function else will execute
        print("Else executed")
