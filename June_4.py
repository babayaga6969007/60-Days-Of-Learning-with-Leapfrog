#Creating a simple calculator in python
print("Please choose between 1.Add, 2.Subtract, 3.Multiply, 4.Divide")
choice = int(input())
if choice == 1:
    num1=int(input("Enter number 1"))
    num2=int(input("Enter number 2"))
    print(num1,"+",num2,"=",num1+num2)
elif choice==2:
    num1=int(input("Enter number 1"))
    num2=int(input("Enter number 2")) 
    print(num1,"-",num2,"=",num1-num2)
elif choice==3:
    num1=int(input("Enter number 1"))
    num2=int(input("Enter number 2"))
    print(num1,"*",num2,"=",num1*num2)
elif choice ==4:
    num1=int(input("Enter number 1"))
    num2=int(input("Enter number 2"))
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Please enter a number between 1 and 4")   


#Other way of creating a simple calculalor
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b   

print("Choose a Selection: 1.Add, 2.Subtract 3. Multiply 4. Divide")
select=int(input("Enter the number doing operation from 1, 2, 3, 4")) 
a=int(input("Enter first number"))   
b=int(input("Enter second number"))    
if select==1:
    print(a,"+", b, "=", add(a, b))
elif select==2:
    print(a, "-", b, "=", sub(a, b))
elif select==3:
    print(a, "*", b, "=", mul(a, b))
elif select==4:
    print(a, "/", b, "=",div(a, b))
else: 
    print("Invalid Input")   
               