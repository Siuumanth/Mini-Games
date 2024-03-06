import random
import time

def get_deposit():
    amount=input("Enter amount to be deposited : $")
    if amount.isdigit():
        amount=int(amount)
        return amount
    else:
        print("Enter a valid amount")
        get_deposit()

def get_bet():
    bet=input("Enter amount to bet $")
    if  bet.isdigit():
        bet=int(bet)
        return bet
    else:
        print("Enter a valid amount")
        get_bet()


def settings():
    symbol_count ={ "A":2 , "B":4, "C":5, "D":6 }
    symbols=[]
    
    for symbol,count in symbol_count.items():
        for i in range(0,count):
            symbols.append(symbol)
    return symbols

def spin(symbols):
    machine=[]
    for i in range(0,9):
        machine.append(symbols[random.randrange(0,len(symbols))])
    for i in range(0,len(machine)):
        if (i+1)%3==0:
            print(machine[i])
        else:
            print(machine[i]+ " | ",end='')
    return machine

def calculate(machine,bet):
    symbol_values={ "A":8, "B":6, "C":3, "D":2 }
    winning=0
    for i in range(0,9,3):
        if(machine[i]==machine[i+1] and machine[i]==machine[i+2]):
            winning+=bet*symbol_values[str(machine[i])]
            
        else:
            winning=0
            
    return winning


def start():
    balance=get_deposit()
    while True:
        bet=get_bet()
        while True:
            if not 1<=bet<=balance:
                print("You cannot bet more than your balance")
                bet=get_bet()
            else:
                break
        balance-=bet
        symbols=settings()
        print("Spinning.....")
        time.sleep(1)
        slots=spin(symbols)
        win=calculate(slots,bet)
        if(win>0):
            print("Congratulations, you won!")
            print("Amount won: $"+str(win))
        else:
            print("OOPS! Better luck next time! \nYou won $0")
        balance+=win
        print("Current balance=$"+ str(balance))
        ch=input("Press enter to play again (q to quit)")
        if ch.lower()=='q':
            print(f"Returning balance of ${balance}")
            print("Thank you for playing!")
            print()
            quit()
        else:
            print("\n")
            continue


start()