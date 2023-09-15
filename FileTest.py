f = open("C:\PythonLearning\DemoFile.txt", "r")
for x in f:
  print(x)
f.close()

f = open("C:\PythonLearning\DemoFile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("C:\PythonLearning\DemoFile.txt", "r")
print(f.read())




