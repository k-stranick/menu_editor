import csv


def load_menu():
    try: # menu would not load needed to add comma between menu.csv and r
        with open('menu.csv', 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_menu(menu):  # not saving
    with open('menu.csv', 'w', newline='') as file:
        columns = ['Name', 'Description', 'Price']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(menu)
def display_menu(menu):  # fixed price display by adding item parameter
    for index_number, item in enumerate(menu):
        print(f"{index_number}. {item['Name']}: {item['Description']} - ${item['Price']}")  # why is it like this
def add_item(menu):
    name = input('Enter item name: ')
    description = input('Enter item description: ') #MUST CAP TO 50 LETTERS
    price = float(input('Enter price: '))
    menu.append({'Name': name, 'Description': description, 'Price': str(price)})  # Maybe string conversion
def edit_item(menu):  # add save function ask question also not working needed to add int to index_function
    display_menu(menu)

    index_number = int(input('Which item would you like to change?: '))
    menu[index_number]["Name"] = input('New item name: ')
    menu[index_number]["Description"] = input('Enter item description: ') #MUST CAP TO 50 LETTERS
    menu[index_number]["Price"] = str(float(input('Enter price: ')))

"""def delete_item():"""
def main():
    menu = load_menu()
    print("test menu program")

    while True:
        display_menu(menu)

        print("\nOptions:")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. Exit")
        choice = input("choose: ")
        if choice == "1":
            add_item(menu)
        elif choice == "2":
            edit_item(menu)
        elif choice == "4":
            save_menu(menu)
            break
if __name__ == "__main__":
    main()