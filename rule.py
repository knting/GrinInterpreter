import random


class Rule:
    def __init__(self, variable, options):
        """takes in a variable and a list of Option Objects"""
        self.variable = variable
        self.options = options

    def pick_random_option(self):
        weights = [option.weight for option in self.options]
        chosen_option = random.choices(self.options, weights = weights, k = 1)[0]
        # print(f'chosen option!!! - {chosen_option}')
        return chosen_option

    def __repr__(self):
        return f"Rule({self.variable}, Options: {self.options})"
