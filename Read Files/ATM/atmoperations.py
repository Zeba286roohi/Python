#atmoperations
from atmexcept import DepositError,WithdrawError,InsufficientFundError
bal=500.00
def deposit():
    damt=float(input("Enter your deposit amount"))#here pvm raises value errorin case of non numneric
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\n Your Account xxxx12 credited with INE{}".format(damt))
        print("Your current Account Balance after deposite INR:{}".format(bal))
        
def withdraw():
    global bal
    wamt=float(input("Enter the withdraw amount"))
    if wamt<=0:
        raise WithdrawError
    elif wamt>bal:
        raise InsufficientFundError
    else:
        bal=bal-wamt
        print("\n Your Account xxxx12 debited with INE{}".format(wamt))
        print("Your current Account Balance after withdraw INR:{}".format(bal))


def balenq(): #as we are not modifying need not write global var
    print("Your current Account Balance INR:{}".format(bal))
    
