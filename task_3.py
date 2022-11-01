# Given two numbers x and n, find the value of x^n (x to the power n)
number=int(input("Whats your number ?"))
power=int(input("Whats the power ? "))

result=1
for item in range(power):
    result=result*number;

print(result)