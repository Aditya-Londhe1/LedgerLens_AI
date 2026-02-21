from datetime import date

import pytest

from app.models import ExpenseCategory, PaymentStatus, SaleItem
from app.store import LedgerStore


def test_full_ledger_flow() -> None:
    store = LedgerStore()

    expense = store.add_expense(
        amount=2500,
        category=ExpenseCategory.ELECTRICITY,
        bill_date=date(2026, 2, 20),
        note="Shop electricity",
    )
    assert expense.id == 1

    sale = store.add_sale(
        customer_name="Ravi",
        customer_phone="9999999999",
        sale_date=date(2026, 2, 21),
        items=[
            SaleItem(name="Oil", quantity=2, unit_price=180),
            SaleItem(name="Rice", quantity=1, unit_price=900),
        ],
        payment_status=PaymentStatus.UNPAID,
    )

    assert sale.total_amount == 1260
    assert sale.sms_sent is True

    summary = store.get_dashboard_summary()
    assert summary.total_expense == 2500
    assert summary.total_sales == 1260
    assert summary.profit == -1240
    assert summary.highest_expense_category == ExpenseCategory.ELECTRICITY


def test_invalid_values_are_rejected() -> None:
    store = LedgerStore()

    with pytest.raises(ValueError):
        store.add_expense(
            amount=0,
            category=ExpenseCategory.OTHER,
            bill_date=date(2026, 2, 21),
        )

    with pytest.raises(ValueError):
        store.add_sale(
            customer_name="Asha",
            customer_phone="9999999998",
            sale_date=date(2026, 2, 21),
            items=[],
            payment_status=PaymentStatus.PAID,
        )
