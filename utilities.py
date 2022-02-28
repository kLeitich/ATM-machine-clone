
from users import users_data

# collect the username, pin
def collect_user_input():
    user_input = {
        'username': None,
        'pin': None
    }

    username = input('What is your username? >>> ')

    for user in users_data:
        cleaned_username = username.capitalize()

        if cleaned_username == user['username']:
            print(f'Welcome back {cleaned_username}!')
            pin = input('Enter your pin: ')
            
            user_input['username'] = cleaned_username
            user_input['pin'] = pin
            return user_input

    print('User not found...')
    return user_input


# check if the username and pin are correct according to our database
def login_user(username, pin):
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