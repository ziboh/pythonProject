#导入模块
import random



# 玩家player出拳,0代表石头，1代表剪刀，2代表布
player = int(input('请输入您的出拳，0代表石头，1代表剪刀，2代表布：'))
# 电脑随机出拳
computer = random.randint(0, 2)
# if嵌套判断结果
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer ==1):
    print('玩家获胜')
elif player == computer:
    print("平局")
else:
    print('电脑获胜')