from .statuses import *


def check(status: Status):
    if type(status) == ExceptionStatus:
        raise status.exception
