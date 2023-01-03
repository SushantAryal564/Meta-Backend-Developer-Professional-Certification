# syntax error are caused by the developer this have the minimum impact cause idm will highlight the error.
#exception this need to be handled.
def divide_by(a,b):
  return a/b;
try:
  ans=divide_by(40,0)
except ZeroDivisionError as e:
  print("We cannot divide by zero")
except Exception as e:
  print(e.__class__);
  print(e);
  
  