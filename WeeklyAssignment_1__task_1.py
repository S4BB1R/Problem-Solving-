numbers = int(input("How many numbers ? : "))
numb = []
n = -1
for item in range(numbers) :
    numb.append(int(input("Insert your number")))

for item in range(numbers-1):
    if numb[item] <= numb[item+1]:
        numb[0]= numb[item]

print(numb[0])