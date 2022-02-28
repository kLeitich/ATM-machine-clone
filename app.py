import re
from users import users_data

# welcome statement
print('Welcome to Lambda Investments Bank')

# user login functionality
# collect the username, pin
def collect_user_input():
    user_input = {
        'username': None,
        'pin': None
    }

    username = input('What is your username? >>> ')
    user_input['pin'] = input('Enter your pin: ')
    user_input['username'] = username.capitalize()

    return user_input

user_input = collect_user_input()

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


result = check_user(user_input['username'], user_input['pin'])

logged_in = False
temp_userdata = None


if (result['wrong_pin'] == True):
    print('You entered the wrong pin...')
    # tell the user to enter the correct pin
    retries_limit = 2
    tries = 0

    while tries < retries_limit:
        # ask them to enter their credentials again
        pin = input('Enter your pin')
        res = check_user(user_input['username'], pin)
        
        if (res['wrong_pin'] == True):
            print('You entered the wrong pin...')
            tries += 1

            if (retries_limit - tries) == 1 :
                print('You only have one more chance...')

            if tries == retries_limit:
                print('Please visit your nearest branch to reset your pin..')
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


print(logged_in)
print(temp_userdata)

# if the username and pin are correct, we set the user to be logged in





# withdraw money

# update the bank balance

# print a receipt

