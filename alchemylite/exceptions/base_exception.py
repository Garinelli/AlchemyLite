class BaseNotProvidedError(Exception):
    """The exception that is thrown if base was not provided"""
    def __init__(self):
        self.message = "Base is required but was not provided"
        super().__init__(self.message)

