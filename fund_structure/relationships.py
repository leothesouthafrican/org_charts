from .entities import FundManager, MasterFund, SubFund, InvestmentVehicle, Investor

def get_entity_details(entity_type):
    name = input(f"Enter the name of the {entity_type}: ")
    attributes = {}
    while True:
        key = input(f"Enter an attribute for the {entity_type} (or press Enter to finish): ")
        if key == "":
            break
        value = input(f"Enter the value for {key}: ")
        attributes[key] = value
    return name, attributes

def add_relationships(parent, child_type):
    children = []
    while True:
        add_child = input(f"Do you want to add a {child_type} under {parent.name}? (yes/no): ")
        if add_child.lower() != 'yes':
            break
        name, attributes = get_entity_details(child_type)
        if child_type == "Master Fund":
            child = MasterFund(name, **attributes)
        elif child_type == "Sub Fund":
            child = SubFund(name, **attributes)
        elif child_type == "Investment Vehicle":
            child = InvestmentVehicle(name, **attributes)
        elif child_type == "Investor":
            child = Investor(name, **attributes)
        parent.add_child(child)
        children.append(child)
    return children
