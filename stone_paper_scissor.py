# stone paper scissor game
import random
l1=['stone','paper','scissor']
cc=0
uc=0
n=1
while n==1:
    for i in range(1,4):
        print("game->",i)
        a=random.choice(l1)
        i=input("please Enter Your move from ['stone','paper','scissor']:")
        print('cpu move=',a)
        print('your move=',i)
        if a=='stone':
            if i=='paper':
                print("you won")
                uc=uc+1
            elif i=='stone':
                print("tie")
            else:
                print("cpu won")
                cc=cc+1
        if a=='paper':
            if i=='paper':
                print("tie")
            elif i=='stone':
                print("cpu won")
                cc=cc+1
            else:
                print("you won")
                uuc=uc+1
        if a=='scissor':
            if i=='paper':
                print("cpu won")
                cc=cc+1
            elif i=='stone':
                print("you won")
                uc=uc+1
            else:
                print("tie")
    if uc>cc:
        print("you won with",uc,'-',cc,'points')
    elif uc==cc:
        print("Tie with",uc,'-',cc,'points')
    else:
        print("Cpu won with",uc,'-',cc,'points')
    n=int(input("Enter 1 to continue or anything to exit:"))