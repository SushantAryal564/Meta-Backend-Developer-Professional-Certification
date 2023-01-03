data = [2,3,4,5,6,7,8,9,10]
data = [x+3 for x in data]
print(data)
print("**************")
newdata= [x*2 for x in data]
print(newdata)
print("***********")
print([x for x in data if x%4 == 0])
print("************")
print([x for x in data if x%4 == 0])
print("***********")
nines = [x for x in range(100) if x%9 ==0]
print(nines)