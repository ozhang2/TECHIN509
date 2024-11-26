from notifications import NotificationMethod

class EmailNotification(NotificationMethod):
    def send(self, messsage):
        print(f"Sending email: {message}")