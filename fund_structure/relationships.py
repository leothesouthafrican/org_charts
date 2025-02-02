# relationships.py

import inquirer
from .entities import FundManager, MasterFund, SubFund, InvestmentVehicle, Investor

# Define common attributes for different entity types
COMMON_ATTRIBUTES = {
    "Fund Manager": ["Experience", "Management Fee"],
    "Master Fund": ["Investment Strategy", "Duration"],
    "Sub Fund": ["Asset Class", "Allocation Percentage"],
    "Investment Vehicle": ["Asset Class", "Risk Level"],
    "Investor": ["Investment Amount", "Investment Date"]
}

def get_entity_details(entity_type):
    questions = [
        inquirer.Text('name', message=f"Enter the name of the {entity_type}"),
    ]
    answers = inquirer.prompt(questions)
    name = answers['name']
    
    attributes = {}
    while True:
        key = inquirer.prompt([
            inquirer.List('attribute', message=f"Select an attribute for the {entity_type} (or select 'Done' to finish)",
                          choices=COMMON_ATTRIBUTES.get(entity_type, []) + ['Done'])
        ])['attribute']
        if key == 'Done':
            break
        value = input(f"Enter the value for {key}: ").strip()
        attributes[key] = value
    
    return name, attributes

def add_relationships(parent, child_type, entities):
    children = []
    while True:
        add_child = inquirer.prompt([
            inquirer.Confirm('add_child', message=f"Do you want to add a {child_type} under {parent.name}?")
        ])['add_child']
        if not add_child:
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
        entities[name] = child  # Store entity by name for cross-referencing
    return children

def link_entities(entities):
    while True:
        link = inquirer.prompt([
            inquirer.Confirm('link', message="Do you want to link two entities?")
        ])['link']
        if not link:
            break
        entity1_name = inquirer.prompt([
            inquirer.List('entity1', message="Select the first entity to link", choices=list(entities.keys()))
        ])['entity1']
        entity2_name = inquirer.prompt([
            inquirer.List('entity2', message="Select the second entity to link", choices=list(entities.keys()))
        ])['entity2']
        if entity1_name != entity2_name:
            entities[entity1_name].add_relationship(entities[entity2_name])
        else:
            print("An entity cannot be linked to itself. Please select different entities.")
