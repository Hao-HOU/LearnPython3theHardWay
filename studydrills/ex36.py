from sys import exit

def start():
    print("接下来你将进行一次探险，你有一个背包，但最多只能装5件东西！")
    print("在探险中你可能获得宝藏，但也有可能丢掉性命！")
    print("你有勇气进行此次探险吗(y/n)？")

    choice = input("> ")

    if choice.upper() == "N":
        print("你选择了退出此次探险！下次见！")
        exit(0)
    elif choice.upper() == "Y":
        print("探险即将开始...")
        game_start()
    else:
        print("指令有误！")
        start()

def game_start():
    bag = ['blue buff', 'red buff']
    print("你将有三条路可以选择，上、中、下路，每条路可能出现")
    print("宝藏的机会与可能会发生危险的，请做出选择")

    choice = input("> ")

    if choice == "上" or choice == "上路":
        print("你选择了上路，祝你好运！")
        top(bag)
    elif choice == "中" or choice == "中路":
        print("你选择了中路，祝你好运！")
        mid(bag)
    elif choice == "下" or choice == "下路":
        print("你选择了下路，祝你好运！")
        bot(bag)
    else:
        print("指令有误！")
        game_start()

def top(bag):
    # TODO: 上路

def mid(bag):
    # TODO: 中路

def bot(bag):
    # TODO: 下路

def check_bag(bag):
    print("背包中现有物品：")
    i = 1
    for good in bag:
        print(i, good)
        i += 1

def throw_away(bag, i):
    good = bag.pop(i)
    print(f"已移出{good}")

start()
