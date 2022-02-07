import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "All day reminder",
            message = "Drink water",
            timeout = 10
        )
        time.sleep(60*60)