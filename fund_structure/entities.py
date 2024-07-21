#entities.py

class Entity:
    def __init__(self, name, **attributes):
        self.name = name
        self.attributes = attributes
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, attributes={self.attributes}, children={self.children})"

class FundManager(Entity):
    pass

class MasterFund(Entity):
    pass

class SubFund(Entity):
    pass

class InvestmentVehicle(Entity):
    pass

class Investor(Entity):
    pass
