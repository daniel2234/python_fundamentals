class Paperboy:
    def __init__(self, name, experience, earnings):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return "{} has {} with {} ".format(self.name, self.experience, self.earnings)

    def quota(self):
        if self.experience <= 50:
            return 50
        elif self.experience >= 50:
            return

    def deliver(self, start_address, end_address):
        pass

    def report(self):
        pass
