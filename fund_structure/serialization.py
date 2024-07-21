import json
from .entities import FundManager, MasterFund, SubFund, InvestmentVehicle, Investor

def entity_to_dict(entity):
    return {
        'name': entity.name,
        'type': entity.__class__.__name__,
        'attributes': entity.attributes,
        'children': [entity_to_dict(child) for child in entity.children]
    }

def save_to_json(fund_manager, filename):
    data = entity_to_dict(fund_manager)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    def dict_to_entity(data):
        entity_type = data.get('type')
        if entity_type == 'FundManager':
            entity = FundManager(data['name'], **data['attributes'])
        elif entity_type == 'MasterFund':
            entity = MasterFund(data['name'], **data['attributes'])
        elif entity_type == 'SubFund':
            entity = SubFund(data['name'], **data['attributes'])
        elif entity_type == 'InvestmentVehicle':
            entity = InvestmentVehicle(data['name'], **data['attributes'])
        elif entity_type == 'Investor':
            entity = Investor(data['name'], **data['attributes'])
        else:
            raise ValueError(f"Unknown entity type: {entity_type}")
        
        entity.children = [dict_to_entity(child) for child in data['children']]
        return entity

    return dict_to_entity(data)
