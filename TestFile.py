import os
name = input("What is your name? ")
file = open("C:/Users/12169/Desktop/Test_File", "x")

file.write("Hello Srini")
print(file.read())

file.close()

print("Hello "+name)
