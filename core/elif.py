age = int(input("Please Enter the age: "))

if age <= 2:
    print("Infant")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")