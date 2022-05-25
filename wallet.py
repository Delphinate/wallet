class Login:
    def __init__(self, login1, password):
        if len(password) < 8:
            password4 = ''
            while True:
                password2 = input('New password: ')
                if len(password2) >= 8:
                    password4 += password2
                    break
            password3 = input('Print password again: ')
            if password4 == password3:
                print('Good')
                print('Your login:', login1)
                print('Your password:', password4)
            else:
                while True:
                    password5 = input('Try again: ')
                    if password5 == password4:
                        print('Good')
                        print('Your login:', login1)
                        print('Your password:', password4)
                        break
        else:
            password6 = input('Print password again: ')
            if password6 == password:
                print('Good')
                print('Your login:', login1)
                print('Your password:', password)
            else:
                while True:
                    password5 = input('Try again: ')
                    if password5 == password:
                        print('Good')
                        print('Your login:', login1)
                        print('Your password:', password)
                        break


print('Password must will have 8-symbols')
log = Login(input('Login: '), input('Password: '))


class Wallet:
    def __init__(self, suma):
        self.money = suma

    def wallet_minus(self, suma):
        if self.money < suma:
            print("You don't have for many money")
            mon1 = 0
            while True:
                try:
                    mon = int(input('How much? '))
                    if mon <= self.money:
                        mon1 += mon
                        break
                except ValueError:
                    print('Money please')
            new_wallet = self.money - mon1
            return new_wallet
        else:
            new_wallet = self.money - suma
            return new_wallet

    def wallet(self):
        return self.money


question = input('If you will want plus the money, press "+": ')
if question == '+':
    while True:
        try:
            money = Wallet(int(input('How much? ')))
            break
        except ValueError:
            print('Money please')
    print('I found in your wallet:', str(money.wallet()) + '$')
    question2 = input('If you will want take the money, press "-": ')
    if question2 == '-':
        while True:
            try:
                print('I found in your wallet:', str(money.wallet_minus(int(input('How much? ')))) + '$')
                print('Exit...')
                break
            except ValueError:
                print('Money please')
    else:
        print('Exit...')
else:
    print('Exit...')
