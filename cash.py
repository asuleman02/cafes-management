import csv

def read_orders_from_csv(file_path):
    orders = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                print(f"Invalid row format: {row}")
                continue
            item = row[0].strip().lower()
            try:
                price = float(row[1])
                quantity = int(row[2])
            except ValueError:
                print(f"Invalid price or quantity in row: {row}")
                continue
            orders.append({
                "item": item,
                "price": price,
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
    input_file = "orders.csv"
    orders = read_orders_from_csv(input_file)
    if not orders:
        print("No valid orders found in the CSV.")
        return
    total_items, subtotal, tax, grand_total = calculate_totals(orders)
    display_summary(total_items, subtotal, tax, grand_total)
    write_output("output_summary.txt", total_items, subtotal, tax, grand_total)
    print("\nSummary written to output_summary.txt")

if __name__ == "__main__":
    main()
