from datetime import date

from .models import ExpenseCategory, PaymentStatus, SaleItem
from .store import LedgerStore


def demo() -> None:
    store = LedgerStore()

    store.add_expense(
        amount=2500,
        category=ExpenseCategory.ELECTRICITY,
        bill_date=date(2026, 2, 20),
        note="Electricity bill",
    )

    store.add_sale(
        customer_name="Ravi",
        customer_phone="9999999999",
        sale_date=date(2026, 2, 21),
        items=[SaleItem(name="Oil", quantity=2, unit_price=180)],
        payment_status=PaymentStatus.UNPAID,
    )

    summary = store.get_dashboard_summary()
    print("Total sales:", summary.total_sales)
    print("Total expense:", summary.total_expense)
    print("Profit:", summary.profit)


if __name__ == "__main__":
    demo()
