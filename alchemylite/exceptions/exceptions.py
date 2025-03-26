class BaseNotProvidedError(Exception):
    """The exception that is thrown if base was not provided."""
    def __init__(self):
        self.message = 'Base is required but was not provided.'
        super().__init__(self.message)

class IncorrectDbmsName(Exception):
    """Exception that occurs when an invalid DBMS type was specified."""
    def __init__(self):
        self.message = 'An incorrect DBMS name was specified.\nDocumentation: link'
        super().__init__(self.message)

class IncorrectConfig(Exception):
    """Exception thrown when specifying invalid config instance in AsyncCrudOperation/SyncCrudOperation"""
    def __init__(self):
        self.message = 'The passed config must be an instance of the SyncConfig/AsyncConfig class.'
        super().__init__(self.message)