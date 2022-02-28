from utilities import collect_user_input, login_user

logged_in = False
temp_userdata = None

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
                temp_userdata = res
                break
    else:
        print('Good to go...')
        logged_in = True
        temp_userdata = result


# # withdraw money

# # update the bank balance

# # print a receipt

