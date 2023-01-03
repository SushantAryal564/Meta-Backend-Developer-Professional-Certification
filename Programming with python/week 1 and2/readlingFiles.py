# read => return entire content of the file as a stirng.
# readline => return a single line as a string
# readline(n) => reads only a specified number of characters in a lne
# readlines => reads teh entire content of the file and returns it in an ordered list.
# with open("text.txt","r") as file:
#   data = (file.readlines())
#   for x in data:
#     print(x);

# import random
# f = open("petnames.txt","r")
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))

list= [1,2,3,4,5]
list[6] = 10;
print(list);