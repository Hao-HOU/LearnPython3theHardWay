from sys import argv

script, filename = argv

print(f"The file {filename} is just created.")
print(f"Now we use {script} to open it.")

txt = open(filename)

print(f"There are some sentences in {filename}:")
print(txt.read())

print("Now we close it.")
txt.close()
