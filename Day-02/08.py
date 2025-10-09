# You can also create if elif ladder using multiple conditions of elif 
# Take the input and check wheather temperature is in celc  ius  Below 0 = freezing cold, 0-10 = very cold, 10-20 = cold, 20-30 = warm, Above 30 = hot, above 40 = very hot

temperature = int(input("Enter the temperature: "))

if temperature < 0:
    print("Freezing cold")
elif temperature >= 0 and temperature < 10:
    print("Very cold")
elif temperature >= 10 and temperature < 20:
    print("Cold")
elif temperature >= 20 and temperature < 30:
    print("Warm")
elif temperature >= 30 and temperature < 40:
    print("Hot")
else:
    print("Very hot")   
