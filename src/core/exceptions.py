class DatabaseConnectionException(Exception):

    def __init__(self):
        self.status_code = 500  # Internal Server Error


class DatabaseException(Exception):
    def __init__(self):
        self.status_code = 500  # Internal Server Error
