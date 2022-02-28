from users import users_data

# welcome statement
print('Welcome to Lambda Investments Bank')

# user login functionality
# collect the username, pin
username = input('What is your username? >>> ')
pin = input('Enter your pin: ')

cleaned_username = username.capitalize()
print(cleaned_username)

# check if the username and pin are correct according to our database
def check_user(username, pin):
    """
    This func takes in a username and a pin and returns userdata if credentials
    are correct. If the credentials are wrong, the return obj will have user set to None
    and wrong_pin set to True
    """
    res = {
        'user': None,
        'wrong_pin': False
    }

    for user in users_data:
        if user['username'] == username:
            # login check password
            if pin == user['pin']:
                res['user'] = user
            else:
                res['wrong_pin'] = True
            break

    return res


result = check_user(cleaned_username, pin)
print(result)


if (result['wrong_pin'] == True):
    print('You entered the wrong pin...')
    # tell the user to enter the correct pin
    retries_limit = 3
    tries = 0


    while tries < retries_limit:
        # ask them to enter their credentials again
        pass



else:
    # set user to logged in
    print('Good to go...')



# if the username and pin are correct, we set the user to be logged in





# withdraw money

# update the bank balance

# print a receipt

