from .rules import BusinessRule

class DomainException(Exception):
    ...

class IsShouldBeInmutable(DomainException):
    def __init__(self, mensaje='Id should be inmutable'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)