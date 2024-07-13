from fund_structure.entities import FundManager
from fund_structure.relationships import add_relationships, get_entity_details
from fund_structure.visualization import visualize_structure

def main():
    # Step 1: Get details for the Fund Manager
    name, attributes = get_entity_details("Fund Manager")
    fund_manager = FundManager(name, **attributes)
    
    # Step 2: Add Master Funds under Fund Manager
    fund_manager.children = add_relationships(fund_manager, "Master Fund")
    
    for master_fund in fund_manager.children:
        # Step 3: Add Sub Funds under each Master Fund
        master_fund.children = add_relationships(master_fund, "Sub Fund")
        for sub_fund in master_fund.children:
            # Step 4: Add Investment Vehicles under each Sub Fund
            sub_fund.children = add_relationships(sub_fund, "Investment Vehicle")
            for vehicle in sub_fund.children:
                # Step 5: Add Investors under each Investment Vehicle
                vehicle.children = add_relationships(vehicle, "Investor")
    
    # Display the structured data
    print("\nStructured Data:")
    print(fund_manager)
    
    # Generate and display the chart
    visualize_structure(fund_manager)

if __name__ == "__main__":
    main()
