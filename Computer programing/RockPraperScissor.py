print("welcome to the game")
import random
pscore=0
cscore=0
while True:
    
    l=["rock","paper","scissor"]
    print("0--rock")
    print("1--paper")
    print("2--scissor")

    pt=int(input("choose your turn "))
    ct=random.randint(0,2)
    print("computer chose ",l[ct] )
    print("you chose ",l[pt] )
    if pt==ct:
        print("draw, both get 1 point")
        cscore+=1
        pscore+=1
    else:
        if ct==0 and pt==1 or ct==1 and pt==2 or ct==2 and pt==0:
            print("player wins")
            pscore+=2
        else:
            print("computer wins")
            cscore+=2

    print("your score is ",pscore)
    print("computer score is ",cscore)
    ch=input("do you want to play again(y/n): ")
    if ch=='n':
        break