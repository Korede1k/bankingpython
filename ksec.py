def username_validator():
    global confirm_username
    username = input('Put in your username: ')
    confirm_username = input('Confirm your username: ')
    if username == confirm_username:
       password_validator()
    else:
        print('Incorrect username, please try again')
        username_validator()


def password_validator():
    global confirm_password
    password = input('Put in your password: ')
    confirm_password = input('Confirm your password: ')
    if password == confirm_password:
       print('Password saved')
       login()
    else:
        print('Incorrect password, please try again')
        
       


def login():
    
    username = input('Put in your username: ') 
    password = input('Put in your password: ')
    if username == confirm_username and password == confirm_password:
        print('Password and Email Verified')
        return
    else:
        print('Incorrect password or email')
        login()
           
        
username_validator()    
        