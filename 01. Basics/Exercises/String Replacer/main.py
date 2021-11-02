username = input('Enter username: ')
password = input('Enter password: ')
password_length = len(password)

masked_password = password_length * '*'

print(f'Hello {username}! Your password {masked_password} is {password_length} letters long')
