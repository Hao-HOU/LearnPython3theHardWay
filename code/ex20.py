from sys import argv # 引入 argv

script, input_file = argv # 赋值给 script 和 input_file

def print_all(f): # 定义函数，输出文件全部内容
    print(f.read())

def rewind(f): # 定义函数，回到文件的开头
    f.seek(0)

def print_a_line(line_count, f): # 定义函数，输出文件的一行
    print(line_count, f.readline(), end = '')

current_file = open(input_file) # 获取文件对象

print("First let's print the whole file:\n") # 提示

print_all(current_file) # 调用该函数，打印输出文件内容

print("Now let's rewind, kind of like a tape.") # 提示

rewind(current_file) # 回到文件的开头，便于下面分行打印

print("Let's print three lines:") # 提示

current_line = 1 # 当前行号
print_a_line(current_line, current_file) # 打印文件中第一行

current_line += 1 # 行号增 1
print_a_line(current_line, current_file) # 答应第二行

current_line += 1 # 行号继续增1
print_a_line(current_line, current_file) # 打印第三行
