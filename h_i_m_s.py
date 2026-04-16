import json
from datetime import datetime
import matplotlib.pyplot as plt

FILENAME = "house_inventory.json"

# ================= LOAD DATA =================
def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

# ================= SAVE DATA =================
def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# ================= ADD ITEM =================
def add_item(data):
    print("\n--- ADD NEW ITEM ---")

    name = input("Item name: ")
    category = input("Category: ")

    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Enter positive value!")
                continue
            break
        except:
            print("Invalid input!")

    while True:
        try:
            daily_use = int(input("Daily usage: "))
            if daily_use < 0:
                print("Enter positive value!")
                continue
            break
        except:
            print("Invalid input!")

    item = {
        "item_name": name,
        "category": category,
        "quantity": quantity,
        "daily_use": daily_use,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(item)
    save_data(data)
    print("Item added successfully!")

# ================= VIEW ITEMS =================
def view_items(data):
    print("\n--- INVENTORY LIST ---")

    if not data:
        print("No items found!")
        return

    for i, item in enumerate(data):
        print(f"\nItem {i+1}")
        print("Name:", item['item_name'])
        print("Category:", item['category'])
        print("Quantity:", item['quantity'])
        print("Daily Usage:", item['daily_use'])
        print("Added On:", item['date_added'])

# ================= DELETE ITEM =================
def delete_item(data):
    view_items(data)

    try:
        index = int(input("Enter item number to delete: ")) - 1
        removed = data.pop(index)
        save_data(data)
        print("Deleted:", removed['item_name'])
    except:
        print("Invalid selection!")

# ================= UPDATE ITEM =================
def update_item(data):
    view_items(data)

    try:
        index = int(input("Enter item number to update: ")) - 1
        item = data[index]

        print("Leave blank to keep old value")

        name = input("New name: ") or item['item_name']
        category = input("New category: ") or item['category']

        qty = input("New quantity: ")
        if qty == "":
            qty = item['quantity']
        else:
            qty = int(qty)

        daily = input("New daily usage: ")
        if daily == "":
            daily = item['daily_use']
        else:
            daily = int(daily)

        item.update({
            "item_name": name,
            "category": category,
            "quantity": qty,
            "daily_use": daily
        })

        save_data(data)
        print("Item updated!")

    except:
        print("Invalid input!")

# ================= SEARCH ITEM =================
def search_item(data):
    key = input("Enter item name to search: ").lower()

    found = False
    for item in data:
        if key in item['item_name'].lower():
            print("\nFound:")
            print(item)
            found = True

    if not found:
        print("Item not found!")

# ================= CATEGORY FILTER =================
def filter_category(data):
    cat = input("Enter category: ").lower()

    for item in data:
        if item['category'].lower() == cat:
            print(item)

# ================= STOCK PREDICTION =================
def predict_stock(data):
    try:
        days = int(input("Enter number of days: "))
    except:
        print("Invalid input!")
        return

    print("\n--- STOCK STATUS ---")

    for item in data:
        remaining = item['quantity'] - item['daily_use'] * days

        if remaining > 0:
            status = "Will last"
        else:
            status = "Will finish"

        print(f"{item['item_name']} -> {status}, Remaining: {remaining}")

# ================= LOW STOCK ALERT =================
def low_stock(data):
    print("\n--- LOW STOCK ITEMS ---")

    for item in data:
        if item['quantity'] < 5:
            print(item['item_name'], "is LOW!")

# ================= PIE CHART =================
def pie_chart(data):
    labels = [item['item_name'] for item in data]
    sizes = [item['quantity'] for item in data]

    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Inventory Distribution")
    plt.show()

# ================= BAR GRAPH =================
def bar_graph(data):
    names = [item['item_name'] for item in data]
    qtys = [item['quantity'] for item in data]

    plt.figure()
    plt.bar(names, qtys)
    plt.title("Quantity Comparison")
    plt.xticks(rotation=45)
    plt.show()

# ================= MAIN MENU =================
def menu():
    data = load_data()

    while True:
        print("\n====== HOUSE INVENTORY SYSTEM ======")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Filter by Category")
        print("7. Predict Stock")
        print("8. Low Stock Alert")
        print("9. Pie Chart")
        print("10. Bar Graph")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_item(data)
        elif choice == "2":
            view_items(data)
        elif choice == "3":
            update_item(data)
        elif choice == "4":
            delete_item(data)
        elif choice == "5":
            search_item(data)
        elif choice == "6":
            filter_category(data)
        elif choice == "7":
            predict_stock(data)
        elif choice == "8":
            low_stock(data)
        elif choice == "9":
            pie_chart(data)
        elif choice == "10":
            bar_graph(data)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

# ================= START =================
if __name__ == "__main__":
    print("Program started at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    menu()