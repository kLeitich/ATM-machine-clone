from utilities import collect_user_input, login_user

logged_in = False
current_balance = None

# welcome statement
print('Welcome to Lambda Investment Bank')

# user login functionality
user_input = collect_user_input()

if not user_input['username'] and not user_input['pin']:
    # we do not need to log them in
    print(
        '''
        Sorry we did not find an account with the given credentials. 
        Please visit a nearby branch to open an account.
        '''
    )
else:
    # we have a username and a pin
    result = login_user(user_input['username'], user_input['pin'])

    # check if the pin is correct
    if (result['wrong_pin'] == True):
        print('You entered the wrong pin...')
        # tell the user to enter the correct pin
        retries_limit = 2
        tries = 0

        while tries < retries_limit:
            # ask them to enter their credentials again
            pin = input('Enter your pin: ')
            res = login_user(user_input['username'], pin)
            
            if (res['wrong_pin'] == True):
                print('You entered the wrong pin...')
                tries += 1

                if (retries_limit - tries) == 1 :
                    print('You only have one more chance...')

                if tries == retries_limit:
                    print('Please visit your nearest branch to reset your pin... Or try again in 24 Hours')
            else:
                # if they entered correct credentials
                print('Good to go...')
                logged_in = True
                current_balance = res['user']['balance']['KSH']
                break
    else:
        print('Good to go...')
        logged_in = True
        current_balance = result['user']['balance']['KSH']



# check balance
def check_balance():
    print(f'Your current balance is {current_balance}')


# withdraw money
def withdraw_money(amount, balance):
    remainder = balance - amount
    if remainder < 0:
        print ('You do have sufficient balance to continue with this transaction')
        return balance
    else:
        print(f'Successfully withdrawn {amount}')
    return remainder



print('Enter W to Withdraw and C to Check Balance')
withdraw_or_check_balance = input('Do you want to withdraw some money or check your balance? (W/C) >>> ')

if withdraw_or_check_balance.upper() == 'W':
    # withdraw some money
    how_much = int(input('How much? >>> '))
    rem = withdraw_money(how_much, current_balance)
    current_balance = rem
    print(f'Your remaining balance is {current_balance}')

elif withdraw_or_check_balance.upper() == 'C':
    # show them the balance
    check_balance()
    response = input('Do you want to withdraw some money? (Y/N) >>> ')
    if response.upper() == 'Y':
        # withdraw some money
        how_much = int(input('How much? >>> '))
        rem = withdraw_money(how_much, current_balance)
        current_balance = rem
        print(f'Your remaining balance is {current_balance}')

    elif response.upper() == 'N':
        print('Thank you for banking wwith us. Have a good Day')
    else:
        print('Invalid input')
else:
    # Invalid input
    print('Invalid input')


# update the bank balance

# print a receipt

