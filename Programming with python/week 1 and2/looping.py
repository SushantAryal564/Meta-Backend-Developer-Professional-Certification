# Python have two looping construct for iterating # over a sequences, the for loop and the while loop.
# str = "Looping";
# for item in str:
#   print(item);

# for i in range(10):
#   print("Looping",i,sep="-");

# favourites = ['Creme Brulee','Apple pie','Churros','Tiramisu','chocolate cake']
# print(tuple(enumerate(favourites,0)))
# for favourite in favourites:
#   print( favourite);
# for idx, favourite in enumerate(favourites):
#   print(idx,favourite,sep="= ")
# count= 0;
# while(count< len(favourites)):
#   print('I like this desert',favourites[count]);
#   count += 1;

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
      continue;
    else:
        print('No sorry, not a dessert on my list')