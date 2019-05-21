"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""

def play(once):
    print("-------------start------------")
    one=random.randint(1, 6)
    two=random.randint(1, 6)
    res=one+two
    print("one is ",one,"two is ",two," ,sum is",res)
    if once!=0:
        print(once)
        if res==once:
            return "win"
        elif res==7:
            return "lose"
        else:
            return play(res)
    else:
        if res==7 or res==11:
            return "win"
        elif res==2 or res==3 or res==12:
            return "lose"
        else :
            return play(res)

import random
decide=(input("do you want to play?"))
if (decide):
    print(play(0))
else:
    print("---------------over----------")
