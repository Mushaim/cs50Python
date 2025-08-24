amount = 50
while True:
    print("Amount Due:",amount)
    due = input()
    if due == "25" or due == "5" or due == "10":
        due = int(due)
    else:
        continue
    amount = amount - due
    if amount <= 0:
        print("Change Owed:", abs(amount))
        break

