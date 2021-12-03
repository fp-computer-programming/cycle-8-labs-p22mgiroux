# Author: MOG 12/3/21

total = 0
while True:
    num = int(input("Please input a number: "))
    if num == -1:
        break
    else:
        total += num
        print(total)