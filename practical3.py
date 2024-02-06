import random 

length = 10
password_output =''
character_set = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*?/-_'
i = 1
while i<=length:
    password_output = password_output + random.choice(character_set)
    i = i+1
print(password_output)