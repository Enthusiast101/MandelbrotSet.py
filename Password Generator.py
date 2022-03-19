# Password Generator:-
import random

variables = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "_:;><.,!@#$%^&*?/\|"
number = "1234567890"


def auto_passwd(inp1, inp2):
    passwd_lst = []
    char = ""

    # 14 digit passcode
    if inp1 == "y":
        for characters in range(0, 50):
            num1 = random.randint(0, len(var_lst) - 1)
            num2 = random.randint(0, len(sym_lst) - 1)
            num3 = random.randint(0, len(num_lst) - 1)
            passwd_lst.append(var_lst[num1])
            passwd_lst.append(sym_lst[num2])
            passwd_lst.append(num_lst[num3])

        random.shuffle(passwd_lst)
        passwd_lst = passwd_lst[0: inp2 + 1]

        for values in range(0, len(passwd_lst) - 1):
            char = char + passwd_lst[values]
        print(char)

        passwd_lst.clear()

    elif inp1 == "n":
        for characters in range(0, 30):
            num1 = random.randint(0, len(var_lst) - 1)
            passwd_lst.append(var_lst[num1])
        random.shuffle(passwd_lst)
        passwd_lst = passwd_lst[0: inp2 + 1]
        char = ""

        for values in range(0, len(passwd_lst) - 1):
            char = char + passwd_lst[values]
        print(char)

    check_passwd(char)


def check_passwd(passwd):
    check_lst = []
    found1, found2, found3 = 0, 0, 0
    ideal = len(passwd) / 6
    for characters in passwd:
        for var in var_lst:
            if characters == var:
                check_lst.append(var)
                found1 += 1
            else:
                continue

        for sym in sym_lst:
            if characters == sym:
                check_lst.append(sym)
                found2 += 1
            else:
                continue

        for num in num_lst:
            if characters == num:
                check_lst.append(num)
                found3 += 1
            else:
                continue
    print(found1, found2, found3, ideal)
    if (found1 and found2 and found3) >= ideal:
        print("Password is strong")
    else:
        print("Password is weak")


while True:
    choice = int(input("press 1 to generate password automatically \npress 2 to enter password manually \n>"))

    var_lst = list(variables)
    sym_lst = list(symbols)
    num_lst = list(number)

    if choice == 1:
        inp1 = input("Do you wish to include numbers and symbols? (y/n)".lower())
        inp2 = int(input("Describe the length of password:- "))

        auto_passwd(inp1, inp2)
        break

    elif choice == 2:
        passwd = input("Enter your password:- ")
        check_passwd(passwd)
        break

    else:
        print("Try again!")
        continue
