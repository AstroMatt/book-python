import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host='example.com',
    user='myusername',
    password='mypassword',
    db='mydatabase',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('myusername@example.com', 'MyVoiceIsMyPassword'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('myusername@example.com',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
