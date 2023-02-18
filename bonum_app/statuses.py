class Status:
    pass


class ExceptionStatus(Status):
    def __init__(self, exception: str | Exception):
        self.exception = exception


class SuccessStatus(Status):
    pass


class Existence:
    pass


class Exists(Existence):
    pass


class NotExists(Existence):
    pass
