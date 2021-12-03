# Author: MOG 12/3/21
x = True
total = 0
while x:
    num = int(input("Please input a number: "))
    if num == -1:
        break
    else:
        total += num
        print(total)