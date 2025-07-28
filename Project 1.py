#snake, water, gun game
""""
snake losses from gun, -1 losses from 1
water looses from snake, 0 looses from -1
gun looses from water, 1 looses from 0
"""
import random as r

def swg():
    x = r.randrange(-1,2)
    # print(x)
    print("snake (s), water (w), gun(g) game")
    choice = str(input("enter your choice: "))
    d = {"s":-1,"w": 0,"g": 1}
    y = d.get(choice)

    if x == y:
        print("Draw!")
    elif (x == -1 and y == 1) or (x == 0 and y == -1) or (x== 1 and y == 0):
        print("You Win!")
    else:
        print("You Loose")
    n = str(input("play again?(y/n)"))
    if n == "y":
        swg()
    else:
        pass
swg()
print("Thanks For Playing")
