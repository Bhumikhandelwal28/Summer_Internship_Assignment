items=[]
prices=[]
while True:
    print("\n Billing Menu")
    print("1. Create Bill")
    print("2. Display Items and Total Bill")
    print("3. Display Total Only")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice==1:
        print("creating Bill")
        n=int(input("enter the number of items"))
        for i in range(n):
            item=input(f"Enter the items {i+1}:")
            price=float(input(f"Enter the price for {item}:"))
            items.append(item)
            prices.append(price)
            print("items added to the bill")
    if choice==2:
        if not items:
            print("The bill is Empty")
        else:
            print("\nItems in Bill:")
            for i in range(len(items)):
                print(f"{items[i]}: {prices[i]:.2f}")
            print(f"Total Amount: {sum(prices):.2f}")

    elif choice == 3:
        print(f"\nTotal Amount: {sum(prices):.2f}")

    elif choice == 4:
        print("Exiting billing program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")