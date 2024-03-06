import random
def roll():
    return random.randint(1,6)

p=int(input("Enter number of players(2-4) "))
scores=[0 for i in range(p)]
temp=0
count=0

while True:
    for i in range(0,len(scores)):
        count=0
        while True:
            print()
            print("P"+str(i+1), "would you like to roll?(y) ")
            ch=input()
            if ch.lower() != 'y':
                scores[i]+=count
                print("chance terminated,score= ",scores[i])
                
                break
            else:
                temp=roll()
                if temp==1:
                    print("you scored a 1 , chance terminated ")
                    break
                else:
                    print()
                    print("you scored a",temp)
                    count+=temp
                    print("your scored ",count,"total = ",count+scores[i])
                    if count+scores[i]>50:
                        print("****PLAYER ", i+1, " YOU WIN****")
                        quit()

                    continue
        

               
           
