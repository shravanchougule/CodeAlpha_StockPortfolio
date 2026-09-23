import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = []

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

while True:

    stock = input("\nEnter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    investment = stock_prices[stock] * quantity

    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": stock_prices[stock],
        "investment": investment
    })

    print(f"Investment value: ${investment}")

    another = input(
        "Do you want to add another stock? (yes/no): "
    ).lower()

    if another != "yes":
        break

print("\n================================")
print("          YOUR PORTFOLIO")
print("================================")

total_investment = 0

for item in portfolio:

    print(
        f"{item['stock']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ${item['price']} | "
        f"Investment: ${item['investment']}"
    )

    total_investment += item["investment"]

print("--------------------------------")
print(f"Total Investment: ${total_investment}")

with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Stock",
        "Quantity",
        "Price",
        "Investment"
    ])

    for item in portfolio:
        writer.writerow([
            item["stock"],
            item["quantity"],
            item["price"],
            item["investment"]
        ])

print("\nPortfolio saved to portfolio.csv")