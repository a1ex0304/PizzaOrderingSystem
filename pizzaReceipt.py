
def generateReceipt(pizzaOrder):
    count = 0
    totalPricenoTax = 0
    totalPrice = 0
    tax = 0.13
    #Assign Variables
    if pizzaOrder == []:
        print("You did not order anything")
        exit()
    #If pizzaOrder is an empty list then it will print out ths and exit out of the code
    else:
        print("Your order: ")
        for i in pizzaOrder:
            sizeOfPizza = ""
            amountOfToppings = 0
            count+=1
            #Assign Varables
            sizeOfPizza = pizzaOrder[count-1][0]
            #Gets the first value of the pizza in the tuple, the first value would be the size of it
            if sizeOfPizza == "S":
                totalPricenoTax += 7.99
                pizzaNumandPrice = ("Pizza " + str(count) + ": " + sizeOfPizza+"7.99".rjust(25))
                #rjust is used format the receipt, so that every price will look organized
                print(pizzaNumandPrice)
                #If the pizza is a small, then it would print out this statement and add $7.99 to the totalPricenoTax
            elif sizeOfPizza == "M":
                totalPricenoTax += 9.99
                pizzaNumandPrice = ("Pizza " + str(count) + ": " + sizeOfPizza+"9.99".rjust(25))
                print(pizzaNumandPrice)
                #If the pizza is a medium, then it would print out this statement and add $9.99 to the totalPricenoTax
            elif sizeOfPizza == "L":
                totalPricenoTax += 11.99
                pizzaNumandPrice = ("Pizza " + str(count) + ": " + sizeOfPizza+"11.99".rjust(25))
                print(pizzaNumandPrice)
                #If the pizza is a large, then it would print out this statement and add $11.99 to the totalPricenoTax
            else:
                totalPricenoTax += 13.99
                pizzaNumandPrice = ("Pizza " + str(count) + ": " + sizeOfPizza+"13.99".rjust(24))
                print(pizzaNumandPrice)
                #If the pizza is a extra large, then it would print out this statement and add $13.99 to the totalPricenoTax
            for topping in pizzaOrder[count-1][1]:
                #This goes to the second value in each pizza in the tuple, that would be the toppings list
                print("- "+topping)
                #Print out each topping
                amountOfToppings+=1
                #Add 1 to the amount of toppings
                if (amountOfToppings>3):
                    #If there are more than 3 toppings in this pizza then it would go to this
                    if sizeOfPizza == "S":
                        totalPricenoTax += 0.50
                        #Add $0.50 for every extra topping for a small pizza
                    elif sizeOfPizza == "M":
                        totalPricenoTax += 0.75
                        #Add $0.75 for every extra topping for a medium pizza
                    elif sizeOfPizza == "L":
                        totalPricenoTax += 1
                        #Add $1 for every extra topping for a large pizza
                    else:
                        totalPricenoTax += 1.25
                        #Add $1.25 for every extra topping for an extra large pizza
            #This is to print out the statement which would indicate that extra toppings were charged
            if amountOfToppings>3:
                #If there are more than 3 toppings on the pizza
                for extraToppings in range(amountOfToppings-3):
                    #Get the amount of extra toppings by subtracting it by 3
                    #We make a for loop with this value
                    #It will print out each corresponding statement for how many extra toppings there are on the pizza
                    if sizeOfPizza == "S":
                        print("Extra Topping (S)" + "0.50".rjust(18))
                    elif sizeOfPizza == "M":
                        print("Extra Topping (M)" + "0.75".rjust(18))
                    elif sizeOfPizza == "L":
                        print("Extra Topping (L)" + "1.00".rjust(18))
                    else:
                        print("Extra Topping (XL)" + "1.25".rjust(17))
        tax = (totalPricenoTax)*(0.13)
        #Get the tax by multipying totalPricenoTax by 0.13
        totalPrice = (totalPricenoTax)+(tax)
        #Add totalPricenoTax and tax
        print("Tax: "+("%.2f"%tax).rjust(30))
        #Print out the tax, rounded to two decimal points
        #Once again rjust is to format the receipt so that every price on it looks organized
        print("Total: "+("%.2f"%totalPrice).rjust(28))
        #Print out the total price, rounded to two decimal points
