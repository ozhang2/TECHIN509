from notifications import NotificationMethod

class SMSNotification(NotificationMethod):
    def send(self, message):
        # use Twilio API
        print(f"Sending SMS: {message}")
        

        

