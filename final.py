print('Welcome to ATM')
restart=('Y')
chances = 3
balance = 67.14
while chances > 0:
    while restart not in ('n','NO','no','N'):
        pin = int(input('Please Enter You 4 Digit Pin: '))
        if pin == (1234):
            print('You entered you pin Correctly\n')
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is Rs.',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = int(input('How Much Would you like to withdraw? \nRs.10\nRs.20\nRs.40\nRs.60\nRs.80\nRs.100 \n press 1 to enter your desired amount'))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    if balance>0:
                        print ('\nYour Balance is now Rs.',balance)
                    else:
                        print("insufficiant balance")
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount:'))
                    balance = balance - withdrawl
                    if balance>0:
                        print ('\nYour Balance is now Rs.',balance)
                    else:
                        print("insufficiant balance")
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = ('y')
                    

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now Rs.',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait whilst your card is Returned...\n')
                print('Thank you for you service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
        elif pin != ('1234'):
            print('Incorrect Password')
            chances = chances - 1
            if chances == 0:
                print('\nNo more tries')
                break