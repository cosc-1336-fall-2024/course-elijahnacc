
def add_inventory(dictionary: dict, widget_name: str, quantity: int):
    
    if widget_name in dictionary:
        dictionary[widget_name] += quantity
    else:
        dictionary[widget_name] = quantity
        
def remove_inventory_widget(dictionary: dict, widget_name: str):

    if widget_name in dictionary:
        del dictionary[widget_name]
        status : str = "Record deleted"
    else:
        status : str = "Item not found"
    
    return status


def display_menu():
    
    print("Inventory Menu\n1 - Add or Update Item\n2 - Delete Item\n3 - Display Current Inventory\n4 - Exit")

def prompt_selection():

    selection = int(input("Enter menu selection: "))

    return selection

def prompt_inventory(selection):

    widget_name = str(input("Enter widget name: "))

    if selection == 1:
        quantity = int(input("Enter quantity: "))
        return widget_name, quantity

    else:
        return widget_name