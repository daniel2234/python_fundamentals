class Paperboy:
    def __init__(self, name, experience=0, earnings=0):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return "{} has {} experience with {} earnings ".format(self.name, self.experience, self.earnings)

    def quota(self):
        min_quota = 50
        if self.experience <= min_quota:
            return min_quota
        elif self.experience >= min_quota:
            return min_quota + (min_quota / 2)

    def deliver(self, start_address, end_address):
        min_quota = 50
        result = end_address - start_address
        additional_route_result = result - min_quota
        total = result - additional_route_result
        return (additional_route_result * .50) + (total * .25)

        # min_quota = 50
        # if end_address - start_address <= min_quota:
        # return (end_address - start_address) * .25
        # elif end_address - start_address >= min_quota:
        #     result = end_address - start_address
        #     subtracted_result = result - min_quota
        #     return (result * .25) + (subtracted_result * .5)

    def report(self):
        pass


tommy = Paperboy("Tommy")

print(tommy)

print(tommy.quota())  # 50


print(tommy.deliver(100, 160))  # 17.5
