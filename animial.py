#Object
# -> Specific intance of a class

# Class
# -> General definition

class iPhone:
    def __init__(self, name, version, phone_number, color, model): # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model 
        self.messages = [] # stored recived messages

    def call(self, number):
        pass
    
    def airdrop(self, filename, recipient):
        print("Dropping %s" % filename)
        pass

    def airreceive(self):
        pass

    def drop(self):
        pass
    def receive(self):
        pass 

# Create an instance of iPhone class
ians_iphone = iPhone(
    name="Ian's iPhone",
    version="18",
    phone_number = "123-123-1232",
    color="qrey",
    model="hi"
)
print(ians_iphone.name)
print(ians_iphone.model)

# rishis_iphone = iPhone(name="Rishi's iPhone")
