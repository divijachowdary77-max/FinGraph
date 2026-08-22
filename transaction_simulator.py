import random
from datetime import datetime

accounts = [f"A{i}" for i in range(501, 521)]
receivers = ["SHELL01", "TARGET01", "B201", "B202", "B203"]

transactions = []

for i in range(20):
    sender = random.choice(accounts)
    receiver = random.choice(receivers)

    while sender == receiver:
        receiver = random.choice(receivers)

    amount = random.randint(500, 10000)

    transaction = {
        "transaction_id": f"T{i+1:03d}",
        "sender_account": sender,
        "receiver_account": receiver,
        "amount": amount,
        "timestamp": datetime.now().isoformat()
    }

    transactions.append(transaction)

import csv

with open("simulated_transactions.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=transactions[0].keys()
    )

    writer.writeheader()
    writer.writerows(transactions)

print("Transactions generated:", len(transactions))
print("CSV saved successfully!")