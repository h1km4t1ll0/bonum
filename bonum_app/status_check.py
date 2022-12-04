from .statuses import *


def check(status) -> ExceptionStatus | SuccessStatus | str:
    if type(status) == ExceptionStatus:
        raise status.exception
    if type(status) == SuccessStatus:
        return 'OK'
    return status
