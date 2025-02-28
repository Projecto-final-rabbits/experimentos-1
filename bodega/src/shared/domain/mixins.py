from .rules import BusinessRule
from .exceptions import BussinessRuleException

class ValidarReglasMixin:
    def validate_rules(self, rules: list[BusinessRule]) -> None:
        for rule in rules:
            if not rule.is_valid():
                raise BussinessRuleException(rule)