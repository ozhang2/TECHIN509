# iPhone class definition
class iPhone:
    def __init__(self, name, version, phone_number, color, model): # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model 
        self.messages = [] # stored recived message
    
    def set_name(self, new_name):
        # change name of iPhone
        self.name = new_name

    def check_messages(self):
        # Prints all received messages
        print(f"Messages for {self.name}:")
        if not self.messages:
            print("No messages.")
        for message in self.messages:
            print(message)

    def send_messages(self, other_iphone, messages):
        # Sends a message to another iPhone
        other_iphone.messages.append(f"From: {self.name}: {messages}")


# Create an instance of iPhone class
phone1 = iPhone(
    name="Oulu's iPhone",
    version="18",
    phone_number="123-123-1231",
    color="Grey",
    model="iPhone 16 Pro",
)

phone2 = iPhone(
    name="Lucy's iPhone",
    version="18",
    phone_number="444-555-6666",
    color="Black",
    model="iPhone 16 Pro",
)

# Change iPhone names
phone1.set_name("Oulu's new iPhone")
phone2.set_name("Lucy's new iphone")

# Send messages between phones
phone1.send_messages(phone2, "Hi Lucy! How's it going?")
phone2.send_messages(phone1, "Hi Oulu! I'm doing well!")

# Check messages on both phones
phone1.check_messages()
phone2.check_messages()