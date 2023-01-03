def sum(*args):
  print(args)
  sum = 0;
  for i in args:
    sum= sum+i;
  return sum;

print(sum(4,5,6,7,8));

def sum_of(**kwargs):
  print(kwargs)
  sum=0;
  for k,v in kwargs.items():
    sum += v
  return round(sum,2)

print(sum_of(coffee=2.99,cake=4.55, juice=2.99))