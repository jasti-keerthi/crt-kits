stock = {}
n = int(input("Enter number of transactions: "))
for i in range(n):
    pid = input("Enter Product ID: ")
    action = input("Enter Action (IN/OUT): ").upper()
    qty = int(input("Enter Quantity: "))
    if pid not in stock:
        stock[pid] = 0
stock[pid] += qty if action == "IN" else -qty if stock[pid] >= qty else 0
print("\nFinal Stock:")
for pid in stock:
    print(pid, ":", stock[pid])