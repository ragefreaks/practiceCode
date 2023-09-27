
import rent as rent,return_cust

print()
print("WELCOME TO COSTUME RENTAL APPLICATION")

option='''

Select desirable option
(1) || Press 1 to rent a custome.
(2) || Press 2 to return a custome.
(3) || Press 3 to exit the app

'''


def displayMessage():
    
    """ Exit Function decided"""
    
    while True:
        
        print(option)

        try:
            choose =int(input("Get an Option for that! "))
            print()

            if(choose == 1):
                print("++++++++++++++++++++++++++++++")
                print("Lets Rent a Costume.")
                print("++++++++++++++++++++++++++++++\n")
                rent.rentCostume()
            
            elif(choose== 2):
                print("++++++++++++++++++++++++++++++")
                print("Lets return a custome")
                print("++++++++++++++++++++++++++++++\n")
                return_cust.mis_cost()
                
            elif(choose == 3):
                print()
                print(" Thanks for using our application")
                print()
                exit()
                
            else:
                print("Not a valid input!!!")
                print("Please select the value as per the provided options")
                print()
        except:
            print("This format is not allowed to attempt....")
            print("Try Again!!")
       
        
            
displayMessage()





