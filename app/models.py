from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum


class ExpenseCategory(str, Enum):
    ELECTRICITY = "electricity"
    STOCK = "stock"
    RENT = "rent"
    SALARY = "salary"
    TRAVEL = "travel"
    OTHER = "other"


class PaymentStatus(str, Enum):
    PAID = "paid"
    UNPAID = "unpaid"


@dataclass(slots=True)
class Expense:
    id: int
    amount: float
    category: ExpenseCategory
    bill_date: date
    note: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class SaleItem:
    name: str
    quantity: int
    unit_price: float


@dataclass(slots=True)
class Sale:
    id: int
    customer_name: str
    customer_phone: str
    sale_date: date
    items: list[SaleItem]
    payment_status: PaymentStatus
    sms_sent: bool
    created_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def total_amount(self) -> float:
        return sum(item.quantity * item.unit_price for item in self.items)


@dataclass(slots=True)
class DashboardSummary:
    total_expense: float
    total_sales: float
    paid_sales: float
    unpaid_sales: float
    profit: float
    highest_expense_category: ExpenseCategory | None
