#Basic Comparison. Keep in mind that python requires intendation while writing code.
print("Enter numbers to compare")
a=int(input("ENter number 1"))
b=int(input("ENter number 2"))
if(a>b):
 print("A is bigger")
else:
 print("B is bigger")


#Write a script that prompts the user to enter base and height of the triangle and 
#calculate an area of this triangle (area = 0.5 x b x h).
print("Enter the base, height of a triangle")
Base=int(input("Enter the base"))
Height=int(input("Enter the height"))
Area=Base*Height*0.5
print("The area of given trianle is ", Area)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')  #True

#Find the length of the text python and convert the value to float and convert it to string
a="python"
print(len(a))
print(float(len(a)))
print(str(len(a)))

#Write a python sript that shows following table:
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125


for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")

#Simple combination of for loop and if/else statement
digits=[1,2,3,4,5,6,7,8,9]
for i in digits:
    if(i%2==0):
     print(i)

#while loop
# program to display numbers from 1 to 5

i = 1
n = 5
while i <= n:
    print(i)
    i = i + 1

