class Calc:
 #create variables
 item1Name = "Apple"
 item1Cost = 0.9
 item1Num = 3

 item2Name = "Mango"
 item2Cost = 1.25
 item2Num = 6

 tax = 0.75

#Find total cost for both items
 item1Total = item1Cost * item1Num
 item2Total = item2Cost * item2Num
 totalBill = item1Total + item2Total

#Total cost with tax
 wTax = totalBill + (totalBill * tax)

#Prints info about first item
 print ("Item 1: " + item1Name)
 print("Cost: " + str(item1Total))
 print("Quantity: " + str(item1Num))

 # Prints info about second item
 print("Item 2: " + item2Name)
 print("Cost: " + str(item2Total))
 print("Quantity: " + str(item2Num))

 print("Tax: " + str(tax))
 print("Total Cost: " + str(wTax))