# logic.py
import random
from templates import *

def generate_question(topic):
    amount = random.randint(5_000, 2_00_000)

    if topic == "Capital Introduction":
        q = random.choice(CAPITAL_TEMPLATES).format(amount=amount)
        sol = (
            "Asset (Cash) increases by ₹{0}\n"
            "Capital increases by ₹{0}\n\n"
            "Assets = Liabilities + Capital ✓"
        ).format(amount)

    elif topic == "Asset Purchase (Cash)":
        asset = random.choice(ASSETS)
        q = random.choice(ASSET_CASH_TEMPLATES).format(asset=asset, amount=amount)
        sol = (
            f"{asset} increases by ₹{amount}\n"
            f"Cash decreases by ₹{amount}\n\n"
            "Total Assets unchanged ✓"
        )

    elif topic == "Asset Purchase (Credit)":
        asset = random.choice(ASSETS)
        q = random.choice(ASSET_CREDIT_TEMPLATES).format(asset=asset, amount=amount)
        sol = (
            f"{asset} increases by ₹{amount}\n"
            f"Liability (Creditor) increases by ₹{amount}\n\n"
            "Assets = Liabilities + Capital ✓"
        )

    elif topic == "Expense Payment":
        expense = random.choice(EXPENSES)
        q = random.choice(EXPENSE_TEMPLATES).format(expense=expense, amount=amount)
        sol = (
            f"Cash decreases by ₹{amount}\n"
            f"{expense} Expense decreases Capital by ₹{amount}\n\n"
            "Assets = Liabilities + Capital ✓"
        )

    elif topic == "Sales (Cash)":
        q = random.choice(SALES_CASH_TEMPLATES).format(amount=amount)
        sol = (
            f"Cash increases by ₹{amount}\n"
            f"Income increases Capital by ₹{amount}\n\n"
            "Assets = Liabilities + Capital ✓"
        )

    elif topic == "Sales (Credit)":
        q = random.choice(SALES_CREDIT_TEMPLATES).format(amount=amount)
        sol = (
            f"Debtors increase by ₹{amount}\n"
            f"Income increases Capital by ₹{amount}\n\n"
            "Assets = Liabilities + Capital ✓"
        )

    else:
        q = "Invalid topic"
        sol = ""

    return q, sol
