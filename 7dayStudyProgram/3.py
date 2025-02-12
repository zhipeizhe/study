import random

def number_guessing_game():
    print("欢迎来到数字猜谜游戏！")
    print("请输入一个1到100之间的数字，我会判断是不是这个数字。")

    # 生成一个1到100之间的随机数
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("请输入你的猜测（按q退出游戏）：")
        if guess == 'q':
            print("游戏结束，谢谢参与！")
            break
        if not guess.isdigit():
            print("请输入一个数字！")
            continue
        if int(guess) < 1 or int(guess) > 100:
            print("请输入一个1到100之间的数字！")
            continue
        guess = int(guess)
        attempts += 1

        if guess == number:
            print("恭喜你，你猜对了！")
            print("你总共猜了", attempts, "次。")
            break
        elif guess < number:
            print("你猜的数字小了，请再试一次！")
        else:
            print("你猜的数字大了，请再试一次！")

if __name__ == '__main__':
    number_guessing_game()
