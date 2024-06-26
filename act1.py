from random import randint

lis = []

def reg():
    userid = randint(00000,99999)
    username = input("Enter username: ")
    password = input("Enter password: ")
    balance = 0
    
    return userid, username, password, balance

def balance(bals):
    print(f"Your balance is : {bals}")

def depo():
    ammount = int(input("Enter ammount to deposit: "))
    return ammount

def minus():
    ammount = int(input("Enter ammount to withdraw: "))
    return ammount

while True:
    print("ENTER (1) TO REGISTER TO OUR BANKING SYSTEM")
    regi = input("")
    if regi == "1":
        var = reg()
        users = {
            "userid" : var[0],
            "username" : var[1],
            "password" : var[2],
            "balance" : var[3]
        }
        lis.append(users)
        # print(lis)
        print(f"Welcome to our banking system {users['username']}\n")
        print(f"User ID: {users['userid']}")
        print("\n -------------------------------------")
        while True:
            user = input("""Enter an action:
                            (1) : CHECK BALANCE
                            (2) : DEPOSIT
                            (3) : WITHDRAW
                            (4) : DELETE ACCOUNT\n""")
            if user == "1":
                balance(users['balance'])
            elif user == "2":
                var = depo()
                users["balance"] += var
            elif user == "3":
                varmi = minus()
                if users["balance"] < varmi:
                    print("Invalid Ammount")
                else:
                    users["balance"] -= varmi
            elif user == "4":
                des = input("Are you sure? ('Yes' if sure): ").lower()
                if des == "yes":
                    print("Thank you for using")
                    break
                else:
                    ...
                break
        break
    else:
        print("Please Register")
