'''This program is meant to work like an online store where customers
can search for their desired product and choose from both new and used
categorties and buy x quantity of it. Sellers can add and delete their
products, add more stocks and view how much they earned through those
products.'''

'''Item data is stored in the form of a list and put into 2 categories
which are also in the form of lists. Users will be asked whether they
are sellers or customers and are then given respective options. Sellers
will be asked a password if they wish to delete or add stock to their
item(s) just like how we, in real life, enter passwords to log into
our accounts to access and edit these details.'''

#The 2 categories below have sample data
#New category takes item name, price, stock, password and units sold
newitems = [['samsung galaxy s20 smart phone', 2999, 100, 'smart', 2],['max tshirt', 25, 50, 'fashion', 16],['jbl bluetooth speakers', 210, 10, 'music', 5],['starry night painting replica of vincent van gogh', 450, 1, 'art', 0],['himalayan lamp', 150, 20, 'lighting', 5],['the great sphinx small sculpture', 99, 7, 'decor', 2],['love yourself bts album', 399, 15, 'kpop', 5],['the fault in our stars book', 45, 35, 'reading', 6],['attack on titan anime eren costume', 300, 2, 'cosplay', 0],['ufc boxing gloves', 50, 10, 'sports', 1],['harry potter slytherin robe', 69, 7, 'cosplay', 3],['adidas blue shoes', 170, 20, 'fashion', 6],['single white stone silver ring', 206, 1, 'jewel', 6],['huawei watchfit smart watch', 20, 14, 'smart', 1]]

'''Used category only takes item name, price and age of product since the
sellers here usually have one piece of the item they no longer need'''
useditems = [['lg 300l refrigerator', 1300, 3],['homecentre 3 seat sofa', 500, 1],['free mulan movie ticket', 0, 0],['ray ban aviator black sunglasses', 50, 0.5],['honda accord car', 30000, 6],['sky land treadmill', 500, 2],['wooden coffee table', 100, 1],['small marble vase', 60, 2.5],['christmas tree', 30, 1],['sony home theatre', 250, 3],['hoover dishwasher', 600, 2],['acoustic guitar', 350, 1],['baby stroller', 50, 3],['2 tennis rackets', 20, 2]]

#Added bank details ie. name, balance and pin needed to access it
bank_data = [['Sania Mulani',50000,9121],['Min Yoongi',1000000,1993],['Troye Sivan',250000,1595],['Jalal Fernandes',1,1234],['Kaneki Ken',999,7753],['Nico Collins',250,2957],['Kim Namjoon',270000,3750],['Mohammed Ali',15000,6666],['Yang Yu Teng',5000,7761],['Alec Benjamin',26000,7721]]
#functions that are called when user chooses respective option
def additem(category):   #takes inputs of item details and adds it to respective category
    global newitems
    global useditems
    itemname = input("Enter item name: ")     
    itemprice = int(input("Enter item price: "))
    found = 0                   #to check whether item with that name already exists
    if category == 'new':
        for i in newitems:
            if itemname.lower() == i[0]:
                found = 1
        if found == 1:
            return "Item already in category"
        else:
            itemstock = int(input("Enter item stock available: "))
            password = input("Enter password to access item: ")
            unitssold = 0
            newlist = [itemname.lower(), itemprice, itemstock, password, unitssold]
            newitems.append(newlist)
            return "Successfully added"
    elif category == 'used':
        for i in useditems:
            if itemname.lower() == i[0]:
                found = 1
        if found == 1:
            return "Item already in category"
        else:
            itemage = int(input("Enter age of item in years: "))
            newlist = [itemname.lower(), itemprice, itemage]
            useditems.append(newlist)
            return "Successfully added"

def addstock(itemname): #adds new units to existing stock
    global newitems
    global useditems
    found = 0  # to check if itemname is in list or not
    for i in newitems:
        if itemname == i[0]:
            found = 1
            password = input("Enter password: ")  #only seller who created this item can change its details
            if password == i[3]:
                units = int(input("Enter no. of units to be added: "))
                i[2] = i[2] + units
                return "Stock successfully added"
            else:
                return "Wrong password"
    if found == 0:
        return "Item not found"
def deleteitem(category):   #deletes item
    global newitems
    global useditems
    itemname = input("Enter item name: ")
    found = 0           # to check if itemname is in list or not
    if category == 'new':
        for i in newitems:
            if itemname.lower() == i[0]:
                found = 1
                password = input("Enter password: ")   #only seller who created this item can delete it
                if password == i[3]:
                    newitems.remove(i)
                    return "Item deleted"
                else:
                    return "Wrong password"
    if category == 'used':
        for i in useditems:
            if itemname.lower() == i[0]:
                found = 1
                useditems.remove(i)
                return "Item deleted"
    if found == 0:
        return "Item not found"
def showsales(itemname):   #returns list with no. of units sold and earnings
    global newitems
    global useditems
    found = 0  # to check if itemname is in list or not
    for i in newitems:
        if itemname == i[0]:
            found = 1
            password = input("Enter password: ")
            if password == i[3]:
                l = [i[4],i[4]*i[1]]
                return l
            else:
                return "Wrong password"
    if found == 0:
        return "Item not found"
def search(keyword, category):  #searches for item with keyword in respective category
    global newitems
    global useditems
    listforreturn = []     #There may be multiple items to return, so we use a list
    if category == 'new':
        for i in newitems:
            if keyword in i[0]:
                listforreturn.append(i)
    elif category == 'used':
        for i in useditems:
            if keyword in i[0]:
                listforreturn.append(i)
    return listforreturn

def buyitem(itemname, category): #eliminates bought units from stock if bank balance is sufficient
    global newitems
    global useditems
    global bank_data
    name = input("Full name: ") #to search for account in bank
    found = 0
    for i in bank_data: #will first check if bank details are present
        if name.title() == i[0]:
            found = 1
            pin = int(input("Enter PIN: "))
            if pin == i[2]:
                if category == 'new':
                    for j in newitems:
                        if itemname == j[0]:
                            units = int(input("How many units would you like to buy? "))
                            if j[2] >= units:
                                if i[1] - j[1]*units >0:
                                    i[1] = i[1] - j[1]*units #deducts spent amount from balance
                                    j[2] = j[2] - units
                                    j[4] = j[4] + units
                                    return "Purchase successful"
                                else:
                                    return "Insufficient Balance"
                            else:
                                return "Stock not available"
                elif category == 'used':
                    for j in useditems:
                        if itemname == j[0]:
                            if i[1] - j[1] >0:
                                i[1] = i[1] - j[1]
                                return "Purchase successful"
                                useditems.remove(j)
                            else:
                                return "Insufficient Balance"
            else:
                return "Wrong PIN"
    if found == 0:
        return "Name not found in bank data"        

choice = 0            #main program starts here
while choice != 3:
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")  #menu with options
    print("*        ONLINE STORE         *")
    print("*******************************")
    print("********** MAIN MENU **********")
    print("*******************************")
    print("Option - 1: I am a seller")
    print("Option - 2: I want to buy products")
    print("Option - 3: Exit")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    choice = int(input("Enter Option no.:"))
    if choice == 1:
        print("*******************************")
        print("Option - 1: Add item")
        print("Option - 2: Add stock (only for new items)")
        print("Option - 3: Delete")
        print("Option - 4: Show profits earned (only for new items)")
        print("*******************************")
        sellerchoice = int(input("Enter Option no.:"))
        category = input("Which category is your product in? (new/used): ")
        if category.lower() in ['new','used']: #to check if input for category is correct
            pass
        else:
            print("Invalid category")
            continue
        if sellerchoice == 1:
            print(additem(category.lower()))
        elif sellerchoice == 2:
            if category.lower() == 'used':
                print("This option is not available for used category")
                continue
            itemname = input("Enter item name: ")
            print(addstock(itemname.lower()))
        elif sellerchoice == 3:
            print(deleteitem(category.lower()))
        elif sellerchoice == 4:
            if category.lower() == 'used':
                print("This option is not available for used category")
                continue
            itemname = input("Enter item name: ")
            l = showsales(itemname.lower()) #returns units sold and earnings
            print("No. of units sold: ", l[0])
            print("Total amount earned: ", l[1])
            
    elif choice == 2:
        category = input("Would you like to search among new or used products? (new/used): ")
        keyword = input("Enter desired product: ")
        if category.lower() in ['new','used']: #to check if input for category is correct
            pass
        else:
            print("Invalid category")
            continue
        listofitems = search(keyword.lower(), category.lower()) #Will get back a list of items from that category having the keyword
        if len(listofitems) == 0:
            print("Not found")
        else:
            for i in listofitems:
                if category.lower() == 'new':
                    print("Name of item: ", i[0])          #Prints each item in respective category containing keyword
                    print("Price: ", i[1])
                    print("Stock available: ", i[2])
                    print("Units sold: ", i[4])
                    print("Index of item: ", listofitems.index(i))
                    print("*******************************")
                elif category.lower() == 'used':
                    print("Name of item: ", i[0])
                    print("Price: ", i[1])
                    print("Age of item: ", i[2])
                    print("Index of item: ", listofitems.index(i))
                    print("*******************************")
            confirmation = input("Is your desired product above? (y/n): ") #Confirming if buyer wants any of the above displayed products  
            if confirmation in ['y','Y']:
                itemindex = int(input("Please type index of desired product: ")) #Index asked to help identify desired product to change stock
                print(buyitem(listofitems[itemindex][0], category.lower()))
    elif choice not in [1,2,3]:
        print("Invalid option")
