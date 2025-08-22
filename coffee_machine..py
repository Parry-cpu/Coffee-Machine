import data_of_coffee as dc

machine_on = True

resources = {"water":300,
             "coffee":100,
             "milk":200,
             "money":0,
             }  

coins_to_dollars = {
    "pennies": 0.01,  # $0.01,
    "nickels":0.05,  # $0.05
    "dimes":0.10,   # $0.1
    "quarters":0.25 # $0.25    
}

def report():
        for i in resources:
            if i =='Coffee':
                print(f"{i}: {resources[i]}gm")
            elif i == "Money":
                 print(f"{i}: ${resources[i]}")
            else:
                print(f"{i}: {resources[i]}ml")
                


def money(drink):

    global resources

    total_money_inserted=0
    total_dollars = 0
    print("Please insert coins!")
    for i in coins_to_dollars:
         money_inserted = int(input(f"How many {i}?: "))
         total_dollars = money_inserted * coins_to_dollars[i]
         total_money_inserted+=total_dollars
         print(f"You inserted {money_inserted} {i} which is ${round(total_dollars,2)} ")
         print(f"Total: ${round(total_money_inserted,2)}")

    print(f"The total money inserted: {round(total_money_inserted,2)}")

    resources["money"]+=dc.MENU[drink]["cost"] 
    ingreditents = resource_calculator(drink)
     

    if total_money_inserted >= dc.MENU[drink]["cost"] and ingreditents == True:
                
         print(f"Here is {round(total_money_inserted-dc.MENU[drink]["cost"],2)} in change")
         return True
    elif ingreditents == False:
         resources["money"]-=dc.MENU[drink]["cost"]
         print(f"Resources left: {resources}")
         return False
    else:
         print(f"Money insufficient for {drink}")
         return False
    

    
def resource_calculator(drink):

    global resources

    

    for i in dc.MENU[drink]["ingredients"]:
        if resources[i]>dc.MENU[drink]["ingredients"][i]:
            resources[i] = resources[i] - dc.MENU[drink]["ingredients"][i]
            print(f"Resources left: {resources}")
            return True
        else:
             print(f"Sorry there is not enough {i}.\nMoney Refunded!")
             return False
    
    


while machine_on:

    screen = input("What would you like? (espresso/latte/cappuccino):")

    if screen == "report":
        report()

    if screen in dc.MENU:
        check = money(screen)
        

    if check ==True:
        print(f"Here is your {screen.title()} ")

    wants_more=input("Do you want anything else?: ").lower()

    if wants_more =="no":
         machine_on = False

