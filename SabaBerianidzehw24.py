#1
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotificationSender(NotificationSender):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotificationSender(NotificationSender):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def send_notification(self, message):
        self.sender.send_notification(message)

email_sender = EmailNotificationSender()
sms_sender = SMSNotificationSender()

email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)

email_service.send_notification("Hello, this is an email notification!")
sms_service.send_notification("Hi, this is an SMS notification!")
