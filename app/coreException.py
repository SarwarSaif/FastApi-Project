from error_code import ErrorCode


class CoreException(Exception):
    def __init__(self, error_code:ErrorCode, message=""): #defalt value of message is none, so can initialize without it
        self.error_code = error_code
        self.message = message
