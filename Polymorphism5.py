class Notification:
    def send(self, message):
        print("Sending notification:", message)


class EmailNotification(Notification):
    def send(self, message):
        print(f"[EMAIL] Sent to inbox: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Text message sent: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"[PUSH] App alert delivered: {message}")


for n in (EmailNotification(), SMSNotification(), PushNotification()):
    n.send("Your order has been shipped!")
