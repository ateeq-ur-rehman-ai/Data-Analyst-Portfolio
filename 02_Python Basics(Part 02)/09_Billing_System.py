# Qno5: Write a program to create a billing a system at supermart.

while True:
    name=input("Enter a customer name: ")
    total=0

    while True:
        print("Enter the amount and the product quantity: ")
        quantity=float(input("Enter the quantity of product: "))
        amount=float(input("Enter the amount of product: "))
        total += quantity*amount

        shop_again= input("Do you want to add more items? (Yes/No): ")
        if shop_again == "no" or shop_again =="NO" or shop_again == "No":
            break

    print("-"*50)
    print("Name: ",name)
    print("Total Bill: ",total)
    print("-"*50)
    print("Thank You ......")
    print("-"*50)

    repeat=input("Do you want to go next customer? (Yes/No): ")
    if repeat == "no" or repeat =="NO" or repeat == "No":
        break
