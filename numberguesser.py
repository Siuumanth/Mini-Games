import random
top=int(input("enter top of range"))
num=-1

ran=random.randint(0,top)
while True:
    num=int(input("enter your guess "))
    if(num>ran):
        print("too high")
    elif(num<ran):
        print("too low")
    if(num==ran):
        print("correct number, ",num)
        break