from faker import Faker


def generate_data():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.first_name()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

print(generate_data())