class RedButton:

    def __init__(self):
        self.click_push = False
        self.fd = -1

    def click(self):
        self.click_push = True
        print("Тревога!")
        self.count()

    def count(self):
        if self.click_push:
            self.fd += 1
        return self.fd


first_button = RedButton()
second_button = RedButton()
for time in range(15):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
