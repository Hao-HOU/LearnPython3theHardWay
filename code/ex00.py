# ex00.py用来做一些额外的练习，比如 Study Drills 中的问题。

# action = input("你最近到底想做什么？")
# when = input("准备什么时候开始？")
#
# print(f"你准备{when}开始{action}！")
#
# num = int(input("请输入一个整数："))
# print(f"你输入的整数是：{num}")

from sys import argv
script, first, second = argv

print("script is", script)
print("first variable is", first)
print("second variable is", second)

name = input("What's your name? ")
print(f"Hello, {name}!")
