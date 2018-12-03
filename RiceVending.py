
line_sep = '----------------------'
rice = float(500)
price = 40
add = 1
buy = 2
buy_kilos = 0
aRice = float(0)
admin = {'username' : 'edselcalanoga',
         'password' : 'Calanoga'}
print('RICE VENDING MACHINE')
print(line_sep)
print('In stock', rice , 'kilos')
print(line_sep)
c = input('Enter 1 if you want to add rice to stock. Enter 2 if you want to buy rice: ')
choice = int(c)

if choice == buy:
    k = input('How many kilos you want to buy? ')
    buy_kilos = float(k)
    print(line_sep)
    m = input('How much money you have? ')
    money = float(m)
    print(line_sep)
    if money == price:
        print('Value verified')
    elif price < money:
        print('Your change: ', money - price)
    else:
        while (money != price):
            if money == price:
                print('Value verified') 
            elif price < money:
                print('Your change: ', money - price)
                break
            print('Money not enough. Insert ' , price-money, ' more')
            m2 = input()
            money2 = float(m2)
            money += money2

elif choice == add:


    uname = input('Username: ')
    usern = str(uname)
    if usern == admin['username']:
        upass = input('Password: ')
        userp = str(upass)
        while userp != admin['password']:
            print('INVALID')
            upass = input('Password: ')
            userp = str(upass)


    while usern != admin['username']:
        print('INVALID')
        uname = input('Username: ')
        usern = str(uname)
        if usern == admin['username']:
            upass = input('Password: ')
            userp = str(upass)
            while userp != admin['password']:
                print('INVALID')
                upass = input('Password: ')
                userp = str(upass)

    print('AUTHENTICATION SUCCESS')
    print(line_sep)
    addRice = input('Insert how much rice you want to add: ')
    aRice = float(addRice)
    print(line_sep)


else:
    print('INVALID INPUT')
    
rice -= buy_kilos
rice += aRice
print('In stock', rice , 'kilos')


