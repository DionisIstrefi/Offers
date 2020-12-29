def divide(x, y):
  return x / y
#Presenting a simple menu.
print("Menu.")

while True:
  choice = input("Offers press (1): ")
#Num1= The price of the item and Num2 the surcharge in % or in decimal exp 0.92.
  if choice in ('1'):
    num1 = float(input("Price: "))
    num2 = float(input("Surcharge: "))

    if choice == '1':
        print(str(num1)+"/"+str(num2)+"="+str(divide(num1, num2)))
#Create a .txt file with results from input.
        with open("output.txt", "w") as msg:
            msg.write(str(num1)+"/"+str(num2)+"="+str(divide(num1, num2)))
            msg.close()
    break
  else:
    print("Invalid Input")
