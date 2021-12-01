#Author: MOG 12/1/21

names = ["Frank", "Mike", "Don", "Shirley"]

def invite(n):
    for x in n:
        print("Hi {}, You're invited to my party on Friday!".format(x))

invite(names)