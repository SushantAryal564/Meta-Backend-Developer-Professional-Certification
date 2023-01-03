def calculateTax(bill,tax_rate):
  return round((bill*tax_rate)/100,2);

print(calculateTax(175,15));  
print(calculateTax(180,12))