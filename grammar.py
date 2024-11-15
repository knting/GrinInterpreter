from input import *
from rule import Rule
from option import Option
from variable import Variable
from terminal import Terminal


class Grammar:
    """Grammar class initiated w attributes lines, num sentences, and start var to run the whole program"""
    def __init__(self, lines, num_sentences, start_var):
        self.lines = lines
        self.num_sentences = int(num_sentences)
        self.start_var = start_var
        self.rules = self.make_rules_objects_list(self.make_rules_list(self.lines))

    @staticmethod
    def make_rules_list(file_lines):
        """Creates a list of tuples where the 0 index is the var name and the 1 index is a list of options."""
        rules_list = []
        options = []
        inside_block = False
        for line in file_lines:
            line = line.strip()
            if line == '{':
                inside_block = True
                options = []  # Start a new block
            elif line == '}':
                if inside_block and options:
                    block_tuple = (options[0], options[1:])
                    rules_list.append(block_tuple)
                inside_block = False
            elif inside_block:
                options.append(line)
        return rules_list

    def make_rules_objects_list(self, rules_list):
        """Creates a Rule object for each rule in the rules list."""
        rule_objs_list = []
        for rule in rules_list:
            variable = rule[0]
            options_list = rule[1]
            op_list = self.make_options_object_list(options_list)
            the_rule = Rule(variable, op_list)
            rule_objs_list.append(the_rule)
        return rule_objs_list

    def make_options_object_list(self, options_list):
        """Creates a list of Option objects from the list of option strings."""
        op_list = []
        for option in options_list:
            weight, *symbols = option.split()
            weight = int(weight)
            symbol_objs = self.make_symbols_object_list(symbols)
            op_list.append(Option(weight, symbol_objs))
        return op_list

    @staticmethod
    def make_symbols_object_list(symbols):
        """Creates a list of Option objects from the list of option strings."""
        symbol_list = []
        for option in symbols:
            if contains_bracketed_symbol(option):
                symbol_list.append(Variable(option[1:-1]))
            else:
                symbol_list.append(Terminal(option))
        return symbol_list

    def execute(self):
        """executes everything"""
        sentences_list = [] # doesn't do anything
        for _ in range(self.num_sentences):
            for rule in self.rules:
                if rule.variable == self.start_var:
                    chosen_option = rule.pick_random_option()
                    if chosen_option:
                        sentence = chosen_option.make_sentence(self)
                        print(sentence)
                        sentences_list.append(sentence)
        # return sentences_list

    def expand_variable(self, variable_name):
        """Expands a variable by finding its rule and generating a sentence."""
        for rule in self.rules:
            if rule.variable == variable_name:
                chosen_option = rule.pick_random_option()
                if chosen_option:
                    return chosen_option.make_sentence(self)


# grammar has rules, rules has options, options have symbols, symbols are either terminals or variables