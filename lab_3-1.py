# Author: MOG 12/2/21

#def sum_to(n):
#    total = 0
#    for i in range(n+1):
#        total += i
#    return total

def sum_to(n):
    i = 0
    total = 0
    while i <= int(n):
        total += i
        i += 1
    return total

value = input("Input your integer: ")
print(sum_to(value))