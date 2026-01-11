from abc import ABC, abstractmethod


class BaseConfig(ABC):
    """
    Abstract base class for database configuration.

    This class provides the basic structure for configuring database connection
    parameters, such as host, port, user, password, and database name. Concrete
    implementations of this class should define the `DATABASE_URL` property and
    the `session` property to establish and manage the database connection.
    """

    @property
    @abstractmethod
    def DATABASE_URL(self) -> str:
        pass

    @property
    @abstractmethod
    def session(self):
        pass


class BaseSQLiteConfig(ABC):
    """Abstract base class for SQLite configuration."""

    @property
    @abstractmethod
    def DATABASE_URL(self) -> str:
        pass

    @property
    @abstractmethod
    def session(self):
        pass
