import random

NumRound = 0
MinRange = 1
MaxRange = 10
# .randint
RandNum = random.randint(MinRange, MaxRange)

while True:
    print(RandNum)
    num = int(input('num enter:'))
    if num == RandNum:
        NumRound += 1
        print("Правильно ", num, ",за ", NumRound, " попыток")
        break
    elif num >= RandNum:
        print("Меньше")
        NumRound += 1
    elif num <= RandNum:
        print("Больше")
        NumRound += 1
