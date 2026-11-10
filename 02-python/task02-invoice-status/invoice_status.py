invoice_id = input("Invoice ID: ").strip()
total_amount = int(input("Total (MKD): "))
amount_paid = int(input("Already paid (MKD): "))
days_overdue = int(input("Days overdue: "))

if invoice_id == "":
    print("Status: INVALID")
    print("Reason: invoice ID cannot be empty.")
elif total_amount <= 0:
    print("Status: INVALID")
    print("Reason: total amount must be a positive integer.")
elif amount_paid < 0:
    print("Status: INVALID")
    print("Reason: paid amount cannot be negative.")
elif days_overdue < 0:
    print("Status: INVALID")
    print("Reason: days overdue cannot be negative.")
else:
    if amount_paid > total_amount:
        status = "OVERPAID"
    elif amount_paid == total_amount:
        status = "PAID"
    elif days_overdue > 0:
        status = "OVERDUE"
    elif amount_paid > 0:
        status = "PARTIALLY_PAID"
    else:
        status = "UNPAID"

    remaining = max(total_amount - amount_paid, 0)

    print(f"Invoice: {invoice_id}")
    print(f"Total: {total_amount:,} MKD")
    print(f"Paid: {amount_paid:,} MKD")
    print(f"Days overdue: {days_overdue}")
    print(f"Status: {status}")
    print(f"Remaining: {remaining:,} MKD")