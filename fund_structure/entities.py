# entities.py

class Entity:
    def __init__(self, name, **attributes):
        self.name = name
        self.attributes = attributes
        self.children = []
        self.relationships = []  # List to store relationships with other entities

    def add_child(self, child):
        self.children.append(child)

    def add_relationship(self, entity):
        self.relationships.append(entity)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, attributes={self.attributes}, children={self.children}, relationships={self.relationships})"

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
