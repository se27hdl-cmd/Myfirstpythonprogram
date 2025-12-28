number = int(input("Choose a number between 1 and 10"))
if number < 1 or number > 10 :
    print("Number is out of the range")
elif number <=5 :
    result = number * 2
    print(f"The result is {result}")
else : 
    result = number + 10
    print(f"The result is {result}")
