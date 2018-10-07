class Solver(object):
    def __init__(self):
        pass

    def rules(self, class_):
        return Rule(class_)

    def variables(self, class_):
        return Variable(class_)

class Rule(object):
    def __init__(self, class_):
        self.class_ = class_

class Problem(object):
    def __init__(self):
        pass

    def add_rule(self):
        pass

    def add_variable(self):
        pass

class Rule(object):
    pass

class Variable(object):
    pass
