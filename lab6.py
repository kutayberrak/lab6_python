import math

# QUESTION 1
while 1:
    n = int(input("Enter the value of n: "))
    x = int(input("Enter the value of x (x>=0): "))
    if x >= 0:
        term = lambda i: (n ** i) / math.factorial(i)
        terms = [term(i) for i in range(x + 1)]
        result = sum(terms)
        break
    else:
        print("x should be grater than or equal to 0: ")
        continue
print(f"Result is: {result}")

# QUESTION 2
def sum_recursive(n):
    global total
    if n == 0:
        print(f"The sum of the series is: {total}")
    else:
        total += ((-1) ** (n + 1)) / n
        sum_recursive(n-1)
while 1:
    n = int(input("Enter the value of n for the second function (n>0): "))
    if n > 0:
        total = 0
        sum_recursive(n)
        break
    else:
        print("n should be grater than 0: ")
        continue
