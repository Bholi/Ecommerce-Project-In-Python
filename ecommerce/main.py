import json

def login():
    pass

def register():
    username = input('Enter your username : ')
    password = input('Enter the password : ')
    usertype = input('Enter your usertype (Buyer/Seller) : ')
    userdata = {
        'username':username,
        'password':password,
        'usertype':usertype,
    }
    json_user_data = json.dumps(userdata)
    f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/userdata.txt','a')
    f.write(json_user_data)
    f.close()


user_choice = input('Do you want to login or register : ')

if  user_choice == 'login':
    pass

elif user_choice =='register':
    register()

else:
    print('Invalid input')