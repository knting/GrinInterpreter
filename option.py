from variable import Variable
from terminal import Terminal


class Option:
    def __init__(self, weight, symbols):
        """Option class initialized with each option's weight and symbols"""
        self.weight = weight
        self.symbols = symbols

    def __repr__(self):
        return f"Option(weight={self.weight}, symbols={self.symbols})"

    def make_sentence(self, grammar):
        """adds the sentence together"""
        return_string = ''
        for symbol in self.symbols:
            if isinstance(symbol, Terminal):
                return_string += (symbol.text + ' ')
            elif isinstance(symbol, Variable):
                rule_variable_name = symbol.rule
                expanded = grammar.expand_variable(rule_variable_name)
                # expanded = grammar.execute(rule_variable_name)
                return_string += (expanded + ' ')
        return return_string.strip()
