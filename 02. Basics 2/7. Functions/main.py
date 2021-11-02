age = 25


def show_age(param):
    print(param)


show_age(age)

# Parameters


def show_name_and_age(name, age):
    print(f'{name} {age}')


show_name_and_age(age=27, name='Danny')

# Default parameters


def show_name_and_age(name, age=18):
    print(f'{name} {age}')


show_name_and_age(name='Lily')
