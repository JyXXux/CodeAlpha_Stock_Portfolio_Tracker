import matplotlib.pyplot as plt
import csv

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

stock_names = []
quantities = []
investment_values = []
total_investment = 0

# ---------------- MENU LOOP ---------------- #
while True:
    print("\n====== STOCK PORTFOLIO TRACKER ======")
    print("1. Add Stock")
    print("2. View Portfolio Summary")
    print("3. Show Portfolio Pie Chart")
    print("4. Save Portfolio to File")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # -------- OPTION 1: ADD STOCK -------- #
    if choice == "1":
        print("\nAvailable Stocks:", stocks)
        stock_name = input("Enter stock name: ").upper()

        if stock_name in stocks:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                else:
                    price = stocks[stock_name]
                    investment = price * quantity

                    stock_names.append(stock_name)
                    quantities.append(quantity)
                    investment_values.append(investment)
                    total_investment += investment

                    print("Stock added successfully!")
            except ValueError:
                print("Invalid quantity. Enter a number.")
        else:
            print("Stock not found.")

    # -------- OPTION 2: VIEW SUMMARY -------- #
    elif choice == "2":
        if len(stock_names) == 0:
            print("\nNo stocks added yet.")
        else:
            print("\n------ Portfolio Summary ------")
            for i in range(len(stock_names)):
                print(f"{stock_names[i]} | Qty: {quantities[i]} | Value: ₹{investment_values[i]}")
            print(f"\nTotal Investment: ₹{total_investment}")

    # -------- OPTION 3: PIE CHART -------- #
    elif choice == "3":
        if len(stock_names) == 0:
            print("\nNo data available for visualization.")
        else:
            plt.figure()
            plt.pie(investment_values, labels=stock_names, autopct='%1.1f%%', startangle=90)
            plt.title("Stock Portfolio Distribution")
            plt.savefig("portfolio_distribution.png")
            print("\n📊 Pie chart saved as 'portfolio_distribution.png'")
            plt.show()

    # -------- OPTION 4: SAVE TO FILE -------- #
    elif choice == "4":
        if len(stock_names) == 0:
            print("\nNo data to save.")
        else:
            filename = input("Enter filename (portfolio.txt or portfolio.csv): ")

            # 🔹 FIX APPLIED HERE (UTF-8 encoding)
            if filename.endswith(".txt"):
                with open(filename, "w", encoding="utf-8") as file:
                    for i in range(len(stock_names)):
                        file.write(
                            f"{stock_names[i]} | Qty: {quantities[i]} | Value: ₹{investment_values[i]}\n"
                        )
                    file.write(f"\nTotal Investment: ₹{total_investment}")
                print("Portfolio saved successfully.")

            elif filename.endswith(".csv"):
                with open(filename, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Stock Name", "Quantity", "Investment Value"])
                    for i in range(len(stock_names)):
                        writer.writerow([stock_names[i], quantities[i], investment_values[i]])
                    writer.writerow(["Total", "", total_investment])
                print("Portfolio saved successfully.")

            else:
                print("Invalid file format.")

    # -------- OPTION 5: EXIT -------- #
    elif choice == "5":
        print("\nThank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
