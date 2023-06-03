#User will enter a floating point number let say 238.915. Your task is to find out the integer
# portion before the point (in this case 238) and then check if that integer portion is an even number or not? ||||||

floating_number=float(input("Enter a floating number"))
round(floating_number)
if(floating_number%2==0):
    print("The inputted number is even")
else:
    print("The inputted number is odd")

#Enter a number upto which the loop will run

a=int(input("Enter the last number"))
i=1
while i<=a:
    print(i)
    i=i+1

#Simple meow game where the user says number in order. However,
#when the number is multuiple of 3 or has number 3 in it, then user says meow.

end_number = int(input("Enter the last number of the series: "))
i = 1
while i <= end_number:
    if i % 3 == 0 or '3' in str(i):
        print("Meow")
    else:
        print(i)
    i += 1
print("Done")

#printing a random number in python using random module

import random
print(random.randint(1,11111))

#Creating a number guesser game:
import random
last_num = int(input("Enter the last number of the range: "))
i = 1
a = random.randint(i, last_num)
guess = int(input("The random number has been generated between your range. Please guess it: "))
while guess != a:
    if guess < a:
        print("The random number is higher than what you chose.")
    else:
        print("The random number is lower than what you chose.")
    guess = int(input("Please guess again: "))

print("Congratulations, you guessed it right!")
print("MISSION SUCCESSFUL")




