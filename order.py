from pizzaReceipt import generateReceipt
#import pizzaReceipt, so they we can use some of its values
TOPPINGS = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE")
pizzaOrder = []
anotherPizza = True
amountOfPizzas = 0
pizza = "Pizza"
#Assign variables
wantToOrder = input("Do you want to order a pizza? ")
if wantToOrder.upper() != "Q" and wantToOrder.upper() != "NO" and wantToOrder!="":
    while True:
        if anotherPizza == True:
            pizzasize = input("Choose a size: ")
            alltoppings = []
            if pizzasize.upper() == "S" or pizzasize.upper() =="M" or pizzasize.upper() =="L" or pizzasize.upper() =="XL":
            #If any of the values are entered, it will go through this
                while True:
                    toppingsChoice = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter 'List'. When you are done adding toppings, enter \"X\"\n")
                    if toppingsChoice.upper() == "LIST":
                        print(TOPPINGS)
                        #Print out toppings if "LIST" is entered
                    elif toppingsChoice.upper() == "X":
                        pizzatuple = (pizzasize.upper(), alltoppings)
                        #Creates a tuple with the size and all toppings
                        pizzaOrder.append(pizzatuple)
                        #Appends it to pizzaOrder
                        amountOfPizzas+=1
                        continueOrder = input("Do you want to continue ordering? ")
                        if continueOrder.upper() == "Q" or continueOrder.upper() == "NO":
                            #If the user doesn't want to continue ordering then it will set the loop to false, this would exit out of both while loops
                            anotherPizza = False
                            break
                        else:
                            #This would only break out of one while loop, allowing the user to still order with the other loop
                            break
                    elif toppingsChoice.upper() in TOPPINGS:
                        #If a topping inputted is a valid topping
                        print("Added", toppingsChoice.upper(),"to your pizza")
                        alltoppings.append(toppingsChoice.upper())
                        #Append the topping into alltoppings
                    else:
                        print("Invalid Topping")
        else:
            #If the while loop is false
            break
    #Go to the generateRecipe if the user doesnt want to order pizza anymore
    generateReceipt(pizzaOrder)
else:
    #If the user doesn't want to get pizza then it would go to the generateReceipt Function
    generateReceipt(pizzaOrder)
