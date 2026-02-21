from collections import defaultdict
from datetime import date

from app.models import (
    DashboardSummary,
    Expense,
    ExpenseCategory,
    PaymentStatus,
    Sale,
    SaleItem,
)


class LedgerStore:
    def __init__(self) -> None:
        self._expense_id = 1
        self._sale_id = 1
        self.expenses: list[Expense] = []
        self.sales: list[Sale] = []

    def add_expense(
        self,
        amount: float,
        category: ExpenseCategory,
        bill_date: date,
        note: str = "",
    ) -> Expense:
        if amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")

        expense = Expense(
            id=self._expense_id,
            amount=amount,
            category=category,
            bill_date=bill_date,
            note=note,
        )
        self.expenses.append(expense)
        self._expense_id += 1
        return expense

    def add_sale(
        self,
        customer_name: str,
        customer_phone: str,
        sale_date: date,
        items: list[SaleItem],
        payment_status: PaymentStatus,
    ) -> Sale:
        if not items:
            raise ValueError("Sale must include at least one item.")
        if any(item.quantity <= 0 or item.unit_price <= 0 for item in items):
            raise ValueError("Item quantity and unit price must be greater than zero.")

        sale = Sale(
            id=self._sale_id,
            customer_name=customer_name,
            customer_phone=customer_phone,
            sale_date=sale_date,
            items=items,
            payment_status=payment_status,
            sms_sent=True,
        )
        self.sales.append(sale)
        self._sale_id += 1
        return sale

    def get_dashboard_summary(self) -> DashboardSummary:
        total_expense = sum(expense.amount for expense in self.expenses)
        total_sales = sum(sale.total_amount for sale in self.sales)
        paid_sales = sum(
            sale.total_amount
            for sale in self.sales
            if sale.payment_status == PaymentStatus.PAID
        )
        unpaid_sales = total_sales - paid_sales

        category_totals: dict[ExpenseCategory, float] = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense.category] += expense.amount

        highest_expense_category = (
            max(category_totals, key=category_totals.get) if category_totals else None
        )

        return DashboardSummary(
            total_expense=total_expense,
            total_sales=total_sales,
            paid_sales=paid_sales,
            unpaid_sales=unpaid_sales,
            profit=total_sales - total_expense,
            highest_expense_category=highest_expense_category,
        )
