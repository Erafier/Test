from faker import Faker


def get_random_person(gender):
    faker = Faker()
    if gender == 'male':
        first_name = faker.first_name_male()
        second_name = faker.first_name_male()
    else:
        first_name = faker.first_name_female()
        second_name = faker.first_name_female()
    return first_name, second_name

