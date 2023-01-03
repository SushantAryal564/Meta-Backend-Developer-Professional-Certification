set_a = {1,2,3,4,5,6,5,6}
set_b = {7,8,9,2,4}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a & set_b)
print(set_a.difference(set_b));
print(set_a - set_b);
print(set_a.symmetric_difference(set_b));
print(set_a ^ set_b)
set_a.add(15)
set_a.remove(1)
set_a.discard(2)
print(set_a)