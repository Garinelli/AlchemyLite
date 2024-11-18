"""
Exception raised when a required base is not provided.

This custom exception is used to signal that a base (which could refer to
a required parameter, attribute, or object) was expected, but not supplied
during the execution of a program.

"""

class BaseNotProvidedError(Exception):
    """The exception that is thrown if base was not provided"""
    def __init__(self):
        self.message = "Base is required but was not provided"
        super().__init__(self.message)

