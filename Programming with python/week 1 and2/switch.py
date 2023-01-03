# also called match statement combine server #contional using | operator
# Match statement compares a value to several #different conditions until one is met
http_status = 500

match http_status:
  case 200:
    print("success");
  case 400:
    print("Bad reqeust")
  case 500 | 501:
    print("server error")
  case 200 | 201:
    print("Success")
  case _:
    print("unknown")
  
  
