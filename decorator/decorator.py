class Notifier():
    def notify(self):
        pass


class BasicNotifier(Notifier):
    notificationText = "BasicNotifier"
    def notify(self):
        return self.notificationText


class AppsNotifierDecorator(Notifier):
    _component = None
    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def notify(self):
        return self._component.notify()


class FacebookNotifier(AppsNotifierDecorator):
    def notify(self):
        return f"u have new message from facebook, notifier based on ({self._component.notify()})"


class TelegramNotifier(AppsNotifierDecorator):
    def notify(self):
        return f"u have new message from telegram, notifier based on ({self._component.notify()})"

class GmailNotifier(AppsNotifierDecorator):
    def notify(self):
        return f"u have new email, notifier based on ({self._component.notify()})"

if __name__ == "__main__":
    basic = BasicNotifier()
    print("basic notifier:")
    print(basic.notify())
    print("\n")

    facebook = FacebookNotifier(basic)
    print(facebook.notify())

    telegram = TelegramNotifier(basic)
    print(telegram.notify())

    gmail = GmailNotifier(basic)
    print(gmail.notify())