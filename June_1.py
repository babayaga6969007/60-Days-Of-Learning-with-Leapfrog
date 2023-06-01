#print("hello")
# This is a comment and nothing is registered when something is written within it.
"""However
when writing multi line comment, above # become unusuable so we use 
"""
"""print("5+3") #stores as string
print(5+3) #shows the result as int
print(5**3) #prints the result of  5^3"""

#Showing Data Type of the written code:
print(type(5)) #Result : Int
print(type("Devashish")) #Result : String
print(type(5.00)) #Result: Float
print(type({5,6,7,8,9})) #Result: Set
print(type([4,5,6,6])) #Result: List
print(type((1,2,3,4,5))) #Result: Tuple
print(type({"Dev":"Anusha", "Yadav" : "Bina"})) #Result: Dictionary

#Length Function
First_name="Devashish"
print(len(First_name))

#Basic Mathematical Operation
a=5
b=6
sum=a+b
print("The sum of " + str(a) + " and " + str(b) + " is ",sum  )

#Taking input from user:
print("Enter two numbers to add")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
sum=a+b
print("The sum of " + str(a)+ " and " + str(b) + " is ",sum)

