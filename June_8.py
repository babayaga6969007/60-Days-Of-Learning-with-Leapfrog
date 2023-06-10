# While loop that prints number from n to n-1th element
n=5
while n > 0:
    print(n)
    n -= 1
print("Completed")


# For loop using range to print from 1 to n value
n=5
for i in range(1, n+1):
    print(i) 


#Using a function to perform a repetitive task
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

result = calculate_sum(10)  # Calculates the sum of numbers from 1 to 10
print(result) 


# Example 4: Solving a problem with iteration
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
