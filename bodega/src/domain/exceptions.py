from src.shared.domain.exceptions import FactoryException

class DoesntExistObjectTypeOnDomain(FactoryException):
    def __init__(self, message="The object type doesn't exist on domain"):
        self.__message = message

    def __str__(self):
        return str(self.__message)
    