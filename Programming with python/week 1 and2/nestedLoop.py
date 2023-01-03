list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
count = 0;
for x in list1:
  for y in list2:
    count +=1;
print(count)
import time
start_time = time.time();
for i in range(10):
  # inner loop
  for j in range(10):
    print(0, end=" ")
  print();
print(round((time.time())-start_time,10))

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0
for ind,num in enumerate(num_list):
  if(num>45):
    print("Over 45")
  elif(num == 36):
    print("Number found at position: ",ind)
    break
  else:
    print("Under 45")
  count += 1;
  
print(count);
  
