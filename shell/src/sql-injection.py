username = input('Username: ')  # User type: ' OR 1=1; DROP TABLE users --
password = input('Password: ')  # User type: whatever

query = f"""

    SELECT id, username, email
    FROM users
    WHERE username='{username}' AND password='{password}'

"""

print(query)
# SELECT id, username, email
# FROM users
# WHERE username='' OR 1=1; DROP TABLE users -- ' AND password='132'
