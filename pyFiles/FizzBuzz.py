oneword = "Fizz"
twoword = "Buzz"

numround = 51

for i in range(numround):
    if i == 0:
        print("Start")
    elif i % 3 == 0 and i % 5 == 0:
        print(i, oneword + twoword)
    elif i % 3 == 0:
        print(i, oneword)
    elif i % 5 == 0:
        print(i, twoword)
    else:
        print(i)
print("End")
