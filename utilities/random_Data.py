from faker import Faker
import random
import string

#we have faker packger using which we get dynamic data
class RandomData:
    def __init__(self):
        self.faker = Faker()

    def get_first_name(self):
        return self.faker.first_name()

    def get_last_name(self):
        return self.faker.last_name()

    def get_full_name(self):
        return self.faker.name()

    def get_email(self):
        return self.faker.email()

    def get_address(self):
        return self.faker.address()

    def get_city(self):
        return self.faker.city()

    def get_state(self):
        return self.faker.state()

    def get_zipcode(self):
        return self.faker.zipcode()

    def get_phone_number(self):
        return self.faker.phone_number()

    def get_company_name(self):
        return self.faker.company()

    def get_random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def get_random_number(self, start=0, end=1000):
        return random.randint(start, end)

