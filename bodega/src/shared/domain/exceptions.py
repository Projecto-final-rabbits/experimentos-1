from .rules import BusinessRule

class DomainException(Exception):
    ...

class BussinessRuleException(DomainException):
    def __init__(self, rule: BusinessRule):
        self.rule = rule
    def __str__(self):
        return str(self.rule)

class IsShouldBeInmutable(DomainException):
    def __init__(self, message='Id should be inmutable'):
        self.__message = message
    def __str__(self):
        return str(self.__message)
    
class FactoryException(DomainException):
    def __init__(self, message):
        self.__message = message
    def __str__(self):
        return str(self.__message)