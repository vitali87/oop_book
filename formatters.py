import datetime
from decimal import Decimal

important = datetime.datetime(2019,10,26, 13,14)

f"{important:%Y-%m-%d %I:%M%p}"

subtotal = Decimal('2.95') * Decimal('1.0625')
template = "{label}: {number:*^{size}.2f}"
template.format(label="Amount", size=10, number=subtotal)

grand_total = subtotal + Decimal('12.34')
template.format(label="Total", size=12, number=grand_total)
