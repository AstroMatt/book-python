class DB:
    _connection = None

    @staticmethod
    def connect():
        if not DB._connection:
            print('Establishing connection...')
            DB._connection = ...

        return DB._connection


# Connecting for the first time
# Will establish new connection
first = DB().connect()

# Connecting for the second time
# Will use existing connection to the DB
# The same handle as `first`
second = DB().connect()
