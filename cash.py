import csv

def load_menu_from_csv(file_path):
    menu = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                print(f"Skipping invalid row: {row}")
                continue
            item = row[0].strip().lower()
            try:
                price = float(row[1])
                quantity = int(row[2])
                menu[item] = {"price": price, "quantity": quantity}
            except ValueError:
                print(f"Invalid data types in row: {row}")
    return menu

def get_orders_from_input(menu):
    orders = []
    print("Enter item names (e.g., 'coffee'). Type 'done' to finish:")
    while True:
        item = input("> ").strip().lower()
        if item == "done":
            break
        if item not in menu:
            print(f"'{item}' not found in menu. Try again.")
            continue
        orders.append({
            "item": item,
            "price": menu[item]["price"],
            "quantity": menu[item]["quantity"]
        })
    return orders

def calculate_totals(orders):
    total_price = 0
    total_items = 0
    for order in orders:
        total = order['price'] * order['quantity']
        total_price += total
        total_items += order['quantity']
    tax = total_price * 0.08
    grand_total = total_price + tax
    return total_items, total_price, tax, grand_total

def display_summary(total_items, subtotal, tax, grand_total):
    print("\nCafe Management System - Order Summary")
    print("--------------------------------------")
    print(f"Total Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (8%): ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")

def write_output(file_path, total_items, subtotal, tax, grand_total):
    with open(file_path, 'w') as file:
        file.write("Cafe Management System - Order Summary\n")
        file.write("--------------------------------------\n")
        file.write(f"Total Items: {total_items}\n")
        file.write(f"Subtotal: ${subtotal:.2f}\n")
        file.write(f"Tax (8%): ${tax:.2f}\n")
        file.write(f"Grand Total: ${grand_total:.2f}\n")

def main():
    menu = load_menu_from_csv("orders.csv")
    if not menu:
        print("Menu could not be loaded. Please check the CSV.")
        return
    orders = get_orders_from_input(menu)
    if not orders:
        print("No valid orders entered.")
        return
    total_items, subtotal, tax, grand_total = calculate_totals(orders)
    display_summary(total_items, subtotal, tax, grand_total)
    write_output("output_summary.txt", total_items, subtotal, tax, grand_total)
    print("\nSummary written to output_summary.txt")

if __name__ == "__main__":
    main()
