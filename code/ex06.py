types_of_people = 10 # 定义一个变量并赋值
x = f"There are {types_of_people} types of people." # 利用 types_of_people 格式化字符串

binary = "binary" # 字符串变量
do_not = "don't" # 字符串变量
y = f"Those who know {binary} and those who {do_not}." # 格式化字符串

print(x) # 打印输出 x
print(y) # 打印输出 y

print(f"I said: {x}") # 使用 x 进行格式化，并输出
print(f"I also said: '{y}'") # 使用 y 进行格式化，并输出

hilarious = False # 布尔变量
joke_evaluation = "Isn't that joke so funny?! {}" # 待格式化语句

print(joke_evaluation.format(hilarious)) # 使用 format() 函数进行格式化

w = "This is the left side of..." # 字符串变量
e = "a string with a right side." # 字符串变量

print(w + e) # 连接 w 和 e，并打印输出
