def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def call_function_ways(count, arg):
    print(f"{count}:", {arg})

count = 0
arg = "10种么？"

call_function_ways(count, arg)
call_function_ways(count + 1, "我觉得可以！")
call_function_ways(2, 67)
call_function_ways(count + 3, len(arg))
temp = input("输入一个整数试试：")
call_function_ways(temp, int(temp))
call_function_ways(f"{arg}", 5)
