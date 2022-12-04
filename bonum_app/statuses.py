class Status:
    pass


class ExceptionStatus(Status):
    def __init__(self, exception: Exception):
        self.exception = exception


class SuccessStatus(Status):
    pass
