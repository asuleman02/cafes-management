import re

# Predefined menu with prices
MENU = {
    "coffee": 3.5,
    "sandwich": 5.0,
    "muffin": 2.25,
    "cookie": 1.25,
    "tea": 2.0
}

def parse_input_line(line):
    """
    Parses lines like 'coffee x3' or 'muffin' and returns (item, quantity)
    """
    line = line.strip().lower()
    match = re.match(r"^([a-z\s]+)(?:\s*x(\d+))?$", line)
    if not match:
        return None, None
    item = match.group(1).strip()
    quantity = int(match.group(2)) if match.group(2) else 1
    return item, quantity

def read_orders_from_input():
    orders = []
    print("Enter items (e.g., 'coffee x2', 'muffin'). Type 'done' to finish:")
    while True:
        line = input("> ").strip()
        if line.lower() == "done":
            break
        item, quantity = parse_input_line(line)
        if item is None or item not in MENU:
            print("Invalid item or format. Please try again.")
            continue
        orders.append({
            "item": item,
            "price": MENU[item],
            "quantity": quantity
        })
    return orders

def calculate_totals(orders):
    total_price = 0
    total_items = 0
    for order in orders:
        total = order['price'] * order['quantity']
        total_price += total
        total_items += order['quantity']
    tax = total_price * 0.08  # 8% tax
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
    orders = read_orders_from_input()
    if not orders:
        print("No orders entered.")
        return
    total_items, subtotal, tax, grand_total = calculate_totals(orders)
    display_summary(total_items, subtotal, tax, grand_total)
    write_output("output_summary.txt", total_items, subtotal, tax, grand_total)
    print("\nSummary written to output_summary.txt")

if __name__ == "__main__":
    main()