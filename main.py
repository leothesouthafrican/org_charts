# main.py

from fund_structure.entities import FundManager
from fund_structure.relationships import add_relationships, get_entity_details
from fund_structure.visualization import FundStructureVisualizer
from fund_structure.serialization import save_to_json, load_from_json

def main():
    # Option to load from an existing JSON file
    choice = input("Do you want to load the fund structure from a JSON file? (yes/no): ").strip().lower()
    if choice == 'yes':
        filename = input("Enter the filename: ").strip()
        if not filename.endswith(".json"):
            filename += ".json"
        fund_manager = load_from_json(filename)
        
        # Allow user to specify node size, font size, and figure size
        node_size = int(input("Enter the desired node size (default 3000): ").strip() or 3000)
        font_size = int(input("Enter the desired font size (default 10): ").strip() or 10)
        figure_width = float(input("Enter the desired figure width (default 10): ").strip() or 10)
        figure_height = float(input("Enter the desired figure height (default 7): ").strip() or 7)
        figure_size = (figure_width, figure_height)

        # Generate and display the chart
        visualizer = FundStructureVisualizer(fund_manager, node_size=node_size, font_size=font_size, figure_size=figure_size)
        visualizer.visualize()
        return  # Terminate the program after generating the plot

    # Step 1: Get details for the Fund Manager
    name, attributes = get_entity_details("Fund Manager")
    if not name:
        name = input("Enter the name of the Fund Manager: ").strip()
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
    
    # Save to JSON file
    filename = input("Enter the filename to save the structure: ").strip()
    if not filename.endswith(".json"):
        filename += ".json"
    save_to_json(fund_manager, filename)

    # Display the structured data
    print("\nStructured Data:")
    print(fund_manager)
    
    # Allow user to specify node size, font size, and figure size
    node_size = int(input("Enter the desired node size (default 3000): ").strip() or 3000)
    font_size = int(input("Enter the desired font size (default 10): ").strip() or 10)
    figure_width = float(input("Enter the desired figure width (default 10): ").strip() or 10)
    figure_height = float(input("Enter the desired figure height (default 7): ").strip() or 7)
    figure_size = (figure_width, figure_height)

    # Generate and display the chart
    visualizer = FundStructureVisualizer(fund_manager, node_size=node_size, font_size=font_size, figure_size=figure_size)
    visualizer.visualize()

if __name__ == "__main__":
    main()
