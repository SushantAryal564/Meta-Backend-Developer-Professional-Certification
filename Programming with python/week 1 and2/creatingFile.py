# File are used to permanently store the data. 
try:
  with open("newfiles.txt",mode="r") as file:
    file.write("\nThis is a new file")
    file.writelines(["\nThis is a another line to be added", "\nnext to another line"])
except FileNotFoundError as e:
  print("Error",e)
  