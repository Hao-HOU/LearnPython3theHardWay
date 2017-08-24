# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

def while_func(r, s):
    # i = 0
    numbers = []
    # while i < r:
    #     print(f"At the top i is {i}")
    #     numbers.append(i)
    #
    #     i = i + s
    #     print("Numbers now: ", numbers)
    #     print(f"At the bottom i is {i}")
    for i in range(0, r, s):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers

print("The numbers:")

for num in while_func(7, 2):
    print(num)
