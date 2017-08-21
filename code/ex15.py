from sys import argv # 从 sys 中引入 argv

script, filename = argv # 将命令行参数赋值给 script 和 filename

txt = open(filename) # 使用 open() 打开文件，并赋值给 txt

print(f"Here's your file {filename}:") # 格式化输出提示
print(txt.read()) # 使用 read() 读取文件中的内容，并打印输出

print("Type the filename again:") # 提示输入
file_again = input("> ") # 再次获取文件名字

txt_again = open(file_again) # 打开新获取的文件名所代表的文件

print(txt_again.read()) # 打印输出新读取的文件内容
