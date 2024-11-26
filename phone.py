class Phone:
    def __init__(self,number):
        self.number = number

    def call(self, to):
        print('Dialing', to, "...")


class iPhone(Phone):
     def airdrop(self, to, file):
          print('Sending', file, 'to', to, '...')

class Android(Phone):
     def ok_google(self):
          print('Ok Google') 

phone = iPhone()
phone.call('123-123-5858')
phone.airdrop()

phone2 = Android()
phone.call('123-123-5858')
phone.okay_google()

# add something