from dictionary import add_inventory, remove_inventory_widget, display_menu, prompt_selection, prompt_inventory

def main():

    user_inventory : dict = {}
    selection : int = 0

    while True:

        display_menu()
        selection = prompt_selection()

        if selection == 4:
            break
        
        if selection == 1:
            widget, quantity = prompt_inventory(selection)
            add_inventory(user_inventory, widget, quantity)

        if selection == 2:
            widget = prompt_inventory(selection)
            status = remove_inventory_widget(user_inventory, widget)
            print(status)

        if selection == 3:
            print(user_inventory)

        
    exit()


if __name__ == '__main__':
    main()