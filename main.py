oneword = "Fizz"
twoword = "Buzz"

numround = 51

for i in range(numround):
    if i == 0:
        print("Start")
    elif i % 3 == 0 and i % 5 == 0:
        print(oneword + twoword)
    elif i % 3 == 0:
        print(oneword)
    elif i % 5 == 0:
        print(twoword)
    else:
        print(i)
print("End")