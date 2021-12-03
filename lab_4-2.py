# Author: MOG 12/3/21

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for x in list:
    if x % 3 != 0:
        continue
    print(x)