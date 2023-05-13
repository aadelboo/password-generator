def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[:3]

    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[:4]

    return user_name

#genrate password from username by switching first and last letter
def password_generator(user_name):
    password = ""
    for letter in range(0, len(user_name)):
        password += user_name[letter - 2] # -2 because we want start from the second last letter and go backwards to the first letter
        print(password)
    return password

password_generator("AbeSimp")
