#There are two file handling method in python open and close. 
# Open function is used for reading, writing and creating file. It requires two argument are filepath or file name and mode.
# Mode set: r,rb,r+,w,a
#close it doens't require any arguments.
# with open function advantages is that it automatically closes the file

file = open("./text.txt",mode="r");
data = file.readline()
print(data)
file.close()

with open ("./text.txt","r") as file:
  data = file.readline()
  print(data)
  