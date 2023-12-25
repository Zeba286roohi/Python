#Atm Demo--main program
from atmmenu import menu
#atmproject--file name and act as module
from atmoperations import deposit,withdraw,balenq
from atmexcept import DepositError,WithdrawError,InsufficientFundError
import sys
def runatm():

    while(True):
        menu()
        try:
            ch=int(input("Enter your choice"))
            match(ch):
                case 1:
                    try:
                        
                        deposit()
                    except ValueError:
                        print("\n Donot try to deposit str,symobols,alphanumerice")
                    except DepositError:
                        print("\n Donot try to deposit negative or zero value")
                case 2:
                    try:
                        
                        withdraw()
                    except ValueError:
                        print("\n Donot try to withdraw str,symobols,alphanumeric")
                    except WithdrawError:
                        print("\n Donot try to withdraaw negative or zero value")
                    except InsufficientFundError:
                        print("\n Your account doesnot have sufficient error")
                        
                case 3:
                    balenq()
                case 4:
                    print("Thanks for using this Application")
                    sys.exit()
                case _:
                    print("Your selection of Operation is wrong Try again")
        except ValueError:
            printt("LICENSE.txttors")
        
