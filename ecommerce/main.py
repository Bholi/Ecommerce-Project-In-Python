# Requirements
# Ask the user to login / register, 
# If login ask for username and password and check if it is a valid user in a file
# If register ask for username, password and usertype(buyer/seller) , then write the data in a file
# If the user is buyer provide the choices of : 1. View product, 2. Purchase product 3. View bills
# If the user is seller provide the choices of : 1. Add product 2. View bills 3. View product

# Add product logic
# Ask the user for product name, description, price, seller
# Then store this data as a relation data in a file

# Purchase product logic
# After the view product logic ask the user for product purchase
# Ask him/her for the name of product he/she wants to purchase and the quantity of purchase
# Find the product which the buyer wants to purchase and get the price of the product then multiply the price with quantity and print it as total for buyer
# Buyer view bill logic
# Get all the bill data from bill.txt and print only those datas whose buyer key has the same value as the login user's name






import json

def addProduct(seller_name):
    product_name = input('Enter the product name : ')
    description = input('Enter the product description : ')
    price = float(input('Enter the product price : '))

    productData = {
        'name': product_name,
        'description': description,
        'price':price,
        'seller_name':seller_name,
    }
    json_product_data = json.dumps(productData)
    f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/products.txt','a')
    f.write(json_product_data + '-')
    f.close()
    print('Data added')

def viewProduct(username):
    f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/products.txt','r')
    a = f.read()
    product_list = a.split('-')
    for i in product_list:
        if i != '':
            product_data = json.loads(i)
            print(product_data['name'])

    
    user_input = input('Do you want to purchase a product ? "Yes" or "No" : ').lower()
    if user_input == 'yes':
        product_name = input('Enter the product name to purchase : ')
        quantity = int(input('Enter the quantity of the product : '))

        for i in product_list:
            if i != '':
                choosed_product = json.loads(i)
                if choosed_product['name'] == product_name:
                    product = choosed_product
                    total_amount = quantity * choosed_product['price']
                    print(f'The total price for {quantity} {product_name}s is Rs.{total_amount}')
        
        bill_data = {
            'product_name': product.get('name'),
            'quantity': quantity,
            'total_price': total_amount,
            'username':username,
        }
        json_bill_data = json.dumps(bill_data)
        f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/bill.txt','a')
        f.write(json_bill_data + '-')
        f.close()

    elif user_input == 'no':
        pass
    f.close()


def view_your_product(seller_name):
    f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/products.txt','r')
    a = f.read()
    f.close()
    list_product_data = a.split('-')
    for i in list_product_data:
        if i != '':
            products = json.loads(i)
            if products.get('seller_name') == seller_name:
                print(i)

def view_bills(user):
    f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/bill.txt','r')
    a = f.read()
    f.close()
    bills_list = a.split('-')
    for i in bills_list:
        if i != '':
            bills = json.loads(i)
            if bills.get('username') == user:
                print(bills)


def login():
    username = input('Enter your username : ')
    password = input('Enter your password : ')
    f = open('/Users/faizansari/Mind Risers/Python Class/ecommerce/userdata.txt','r')
    a = f.read()
    user_list_data =  a.split('-')
    user_login = False
    user_type = None
    for i in user_list_data:
        if i != '':
            dict_data = json.loads(i)
            if dict_data.get('username') == username and dict_data.get('password') == password:
                user_login = True
                user_type = dict_data
    if user_login == True:
        print('Login Successful')
        if user_type.get('usertype') == 'seller':
            print('''
                1. Add Product
                2. View Bills
                3. View Your Products
            ''')
            user_operation = int(input('Enter the operation you want to perform : '))
            if user_operation == 1:
                addProduct(user_type.get('username'))
            elif user_operation == 3:
                view_your_product(user_type.get('username'))

        elif user_type.get('usertype') == 'buyer':
            print('''
                1. View Products
                2. Purchase product
                3. View Your Bills
            ''')
            user_operation = int(input('Enter the operation you want to perform : '))
            if user_operation == 1:
                viewProduct(user_type.get('username'))
            
            elif user_operation == 3:
                view_bills(user_type.get('username'))

            
    else:
        print('Invalid credentials')

    f.close()

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
    f.write(json_user_data + '-')
    f.close()


user_choice = input('Do you want to login or register : ')

if  user_choice == 'login':
    login()

elif user_choice =='register':
    register()

else:
    print('Invalid input')