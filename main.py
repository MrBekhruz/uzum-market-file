import json

def save_items(item_category, item_name, item_seller, item_dastavka, item_price, item_quantity, item_assessments, item_order, nasiya):
    with open('item_databas.json', 'a') as file:
        data = {
            'item_category': item_category,
            'item_name': item_name,
            'item_seller': item_seller,
            'item_dastavka': item_dastavka,
            'item_price': item_price,
            'item_quantity': item_quantity,
            'item_assessments': item_assessments,
            'item_order': item_order,
            'nasiya': nasiya
        }
        json.dump(data, file)
        file.write('\n')

def load_database():
    try:
        with open('item_databas.json', 'r') as file:
            lines = file.readlines()
            database = [json.loads(line) for line in lines]
            return database
    except FileNotFoundError:
        return []

def get_user_input():
    user_input = input("Enter the name of item: ")
    return user_input

def ask_item(user_input, database):
    for entry in database:
        if entry['item_name'] == user_input:
            return entry

def filter_by_category(category, database):
    filtered_items = []
    for entry in database:
        if entry['item_category'] == category:
            filtered_items.append(entry)
    return filtered_items

def buyer(item_name, item_quantity, item_price):
    name = input("Enter the name of the item you want to buy: ")
    if name == item_name:
        quantity = int(input(f"Enter the quantity of {name} to buy: "))
        if quantity > item_quantity:
            print("Error! This quantity exceeds available stock.")
        else:
            total_cost = item_price * quantity
            print(f"You bought {quantity} {item_name}(s) for {total_cost} so'm")

def main():
    filter_choice = input("Do you want to filter by category? (yes/no): ").lower()
    if filter_choice == 'yes':
        category_to_filter = input("Enter the category to filter by: ")
        database = load_database()
        filtered_items = filter_by_category(category_to_filter, database)
        if filtered_items:
            print(f"Filtered items for category {category_to_filter}:")
            for entry in filtered_items:
                print(entry)
        else:
            print("No items found in the specified category")
    else:
        while True:
            choice = input("Choose 'seller' or 'buyer': ").lower()
            if choice == 'seller':
                print("You chose seller.")
                break
            elif choice == 'buyer':
                database = load_database()
                user_input = get_user_input()
                item = ask_item(user_input, database)
                if item:
                    buyer(item['item_name'], item['item_quantity'], item['item_price'])
                    break
                else:
                    print("Sorry, item not found.")
                    continue
            else:
                print("Invalid choice. Please choose 'seller' or 'buyer'.")

if __name__ == '__main__':
    main()
