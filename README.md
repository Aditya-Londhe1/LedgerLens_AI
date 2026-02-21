# LedgerLens AI - Invoice & Expense Tracker for Small Shops

This is the **first working backend/core build** for an AI Invoice & Expense Tracker.
It focuses on core business logic for shopkeepers:

- expense ledger,
- sale transaction records,
- customer receipt/payment status,
- and profit/loss summary.

## What is implemented now

- Add expenses with category, bill date, and notes
- Add customer sales with itemized products
- Auto-calculate sale total
- Track payment status (`paid` / `unpaid`)
- Mark receipt dispatch status (`sms_sent` flag)
- Generate dashboard totals:
  - total expenses
  - total sales
  - paid sales
  - unpaid sales
  - profit
  - highest expense category

## Project structure

- `app/models.py` - domain models (expense, sale, summary)
- `app/store.py` - in-memory ledger store + business logic
- `app/main.py` - simple runnable demo flow
- `tests/test_store.py` - tests for happy-path and validation cases

## Run demo

```bash
python -m app.main
```

## Run tests

```bash
pytest
```

## Next steps (from your product idea)

- bill photo upload
- OCR for invoice reading (amount/date/items)
- auto expense categorization with AI
- SMS integration for sending customer receipt
- GST-ready exports (CSV/PDF)
- mobile app integration (Flutter/React Native)
- shop-wise login and cloud sync
