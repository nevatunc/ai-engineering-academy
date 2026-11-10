# Invoice Status Assistant v0.1

Name: Nezaket Neva Tunç
Eduperia AI Engineering Academy - Assignment 02 (Python Fundamentals I)

## What is this project?

This is a small command-line program that checks the status of an invoice. The user enters an invoice ID, the total amount, the amount already paid and the number of days overdue. The program checks the values, decides the status of the invoice and prints a short report with the remaining amount.

The program only uses simple rules (if / elif / else). It does not use any machine learning. All data in the tests is made up.

## How to run it

You need Python 3.11 or newer.

```
cd 02-python/task02-invoice-status
python3 invoice_status.py
```

Then type the four values when the program asks for them.

## Input rules

- Invoice ID: cannot be empty
- Total amount: must be a positive whole number (MKD)
- Amount paid: cannot be negative
- Days overdue: cannot be negative (0 means not overdue)

If one of these is wrong, the program prints `Status: INVALID` and a message that explains why.

## How the status is chosen

The rules are checked in this order, and the first one that matches is used:

1. Invalid input -> INVALID
2. Paid is more than total -> OVERPAID
3. Paid is equal to total -> PAID
4. Paid is less than total and days overdue is more than 0 -> OVERDUE
5. Some amount is paid and it is not overdue -> PARTIALLY_PAID
6. Nothing is paid and it is not overdue -> UNPAID

The remaining amount is `max(total - paid, 0)`, so it is never negative.

## Assumptions

- All amounts are whole numbers in MKD.
- The user types numbers for the number fields. The program does not handle text like "abc" yet (try/except could be added later).
- Only fake invoice data is used.

## Example

Input: `INV-101`, `12000`, `4000`, `8`

```
Invoice: INV-101
Total: 12,000 MKD
Paid: 4,000 MKD
Days overdue: 8
Status: OVERDUE
Remaining: 8,000 MKD
```

## Tests

I tested the 7 required cases (T1 to T7). The inputs and results are in `test_evidence.txt`.