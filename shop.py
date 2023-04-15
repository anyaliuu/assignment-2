#Developed by Anya Liu
#Date: March 8
#Desc: A program to take user inputs and output the prices of the PC's they're purchasing
#Inputs: Numbers corresponding to the ID's of each PC component and pre-built PC's
#Outputs: A list containing the total price for each PC the user wants to purchase

#lists contatining the ID's, name, and price of each component/pre-built PC
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]

#helper function that prints a string for each list
def printListOptions(list):
        for entry in list:
            print(entry[0], ":", entry[1] + ",", entry[2])

#helper function that appends only the ID's of each component/pre-built to a list
def extract(list):
    ID_list = []
    for entry in list:
        element = (entry[0])
        ID_list.append(element)
    return sorted(ID_list)

print("Hi, welcome to my PC shop!")

#function to run the program
def pickItems():

    #empty list to append the price of each PC
    item_prices = []

    while (True):

        #variables that store the prices of custom-built and pre-built PC's
        total_price = 0
        total_price_prebuilt = 0

        orderCategory = input('\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ')
        if (orderCategory == '1'):

            print('\nGreat! Let\'s start building a custom PC!')
#CPU
            print('\nFirst, let\'s pick a CPU.')
            printListOptions(CPU)
            #while loop that keeps prompting the user for a valid input if they enter something invalid
            valid = False
            while not valid:
                CPU_pick = str(input("Choose the number that corresponds with the part you want: "))
                if CPU_pick in extract(CPU):
                    valid = True
            #adds the price of the component to the total price of the PC
            if CPU_pick == '1':
                total_price += CPU[0][2]
            else:
                total_price += CPU[1][2]
#MOTHERBOARD
            print('\nNext, let\'s pick a compatible motherboard.')
            #if-else statement to make sure the MOTHERBOARD the user can pick will be compatible to the CPU they picked previously
            if CPU_pick == '1': #if user enters '1' for CPU, MOTHERBOARD has to be MSI Z490-A PRO
                print(MOTHERBOARD[1][0], ":", MOTHERBOARD[1][1] + ",", "262.30")
                valid = False
                while not valid:
                    MOTHERBOARD_pick = str(input("Choose the number that corresponds with the part you want: "))
                    if MOTHERBOARD_pick == '2':
                        valid = True
                total_price += MOTHERBOARD[1][2]
                #print total_price to check
            else: #if user enters '2' for CPU, MOTHERBOARD has to be MSI B550-A PRO
                print(MOTHERBOARD[0][0], ":", MOTHERBOARD[0][1] + ",", MOTHERBOARD[0][2])
                valid = False
                while not valid:
                    MOTHERBOARD_pick = str(input("Choose the number that corresponds with the part you want: "))
                    if MOTHERBOARD_pick == '1':
                        valid = True
                total_price += MOTHERBOARD[0][2]
#RAM
            print('\nNext, let\'s pick your RAM.')
            printListOptions(RAM)

            valid = False
            while not valid:
                RAM_pick = str(input("Choose the number that corresponds with the part you want: "))
                if RAM_pick in extract(RAM):
                    valid = True

            if RAM_pick == '1':
                total_price += RAM[0][2]
            else:
                total_price += RAM[1][2]
#PSU
            print('\nNext, let\'s pick your PSU.')
            printListOptions(PSU)

            valid = False
            while not valid:
                PSU_pick = str(input("Choose the number that corresponds with the part you want: "))
                if PSU_pick in extract(PSU):
                    valid = True

            if PSU_pick == '1':
                total_price += PSU[0][2]
#CASE
            print('\nNext, let\'s pick your case.')
            printListOptions(CASE)

            valid = False
            while not valid:
                CASE_pick = str(input("Choose the number that corresponds with the part you want: "))
                if CASE_pick in extract(CASE):
                    valid = True

            if CASE_pick == '1':
                total_price += CASE[0][2]
            else:
                total_price += CASE[1][2]
#SSD
            print('\nNext, let\'s pick an SSD (optional, but you must have at least one SSD or HDD.)')
            printListOptions(SSD)

            valid = False
            while not valid:
                SSD_pick = str(input("Choose the number that corresponds with the part you want: "))
                if (SSD_pick in extract(SSD)) or (SSD_pick == 'x' or SSD_pick == 'X'): #the use can enter 'x' or 'X' if they don't want an SSD
                    valid = True

            if SSD_pick == '1':
                total_price += SSD[0][2]
            elif SSD_pick == '2':
                total_price += SSD[1][2]
            elif SSD_pick == '3':
                total_price += SSD[2][2]
#next HDD

            print('\nNext, let\'s pick an HDD (optional, but you must have at least one SSD or HDD.)')
            printListOptions(HDD)

            if SSD_pick == 'x' or SSD_pick == 'X': #if user entered 'x' or 'X' for SSD, must pick an HDD
                valid = False
                while not valid:
                    HDD_pick = str(input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): "))
                    if HDD_pick in extract(HDD):
                        valid = True
            else: #if user picked an SSD, have option to either purchase or not purchase an HDD
                HDD_pick = str(input("Choose the number that corresponds with the part you want: "))
                while HDD_pick not in ['1', '2', 'x', 'X']:
                    print(HDD_pick)
                    HDD_pick = str(input("Choose the number that corresponds with the part you want: "))

            if HDD_pick == '1':
                total_price += HDD[0][2]
            else:
                total_price += HDD[1][2]

#GRAPHICS
            print('\nFinally, let\'s pick your graphics card (or X to not get a graphics card).')
            printListOptions(GRAPHICS_CARD)

            valid = False
            while not valid:
                value = str(input("Choose the number that corresponds with the part you want: "))
                if value in extract(GRAPHICS_CARD):
                    valid = True
                elif value == 'x' or value == 'X':
                        valid = True

                if value == '1':
                    total_price += GRAPHICS_CARD[0][2]

                #prints total price of the custom-built PC
                print('\nYou have selected all your required components! Your total for the PC is $%.2f' % total_price)

            item_prices.append(round(total_price, 2))
#pre-built PC
        elif (orderCategory == '2'):

            print('\nGreat! Let\'s pick a pre-built PC!')

            print('\nWhich pre-built PC would you like to purchase?')
            printListOptions(PREBUILTS)

            valid = False
            while not valid:
                value = str(input("Choose the number that corresponds with the part you want: "))
                if value in extract(PREBUILTS):
                    valid = True

            if value == '1':
                total_price_prebuilt += PREBUILTS[0][2]
            elif value == '2':
                total_price_prebuilt += PREBUILTS[1][2]
            elif value == '3':
                total_price_prebuilt += PREBUILTS[2][2]

            #prints the total price for the pre-built PC
            print('\nYour total price for this pre-built is $%.2f' % total_price_prebuilt)

            item_prices.append(round(total_price_prebuilt, 2))

        elif (orderCategory == '3'):

            #returns the list of the total prices of all the PC's the user wants to purchase
            return item_prices

print(pickItems())