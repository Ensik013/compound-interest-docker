"""Практична робота №5, варіант 1: калькулятор складних відсотків.

Автор: Кульомін Нікіта, група З-41, номер у списку 21.

Вхідні дані беруться зі змінних середовища:
  SUM          - початкова сума вкладу, грн (> 0)
  RATE         - річна відсоткова ставка, % (>= 0)
  PERIODS      - кількість років (ціле, >= 1)
  COMPOUNDING  - скільки разів на рік нараховуються відсотки (ціле, >= 1; 1 = раз на рік, 12 = щомісяця)
"""
import os
import sys
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

CENT = Decimal("0.01")


def read_number(name, default, integer=False):
    raw = os.environ.get(name, default)
    try:
        value = Decimal(raw.replace(",", "."))
    except InvalidOperation:
        raise ValueError(f"{name}='{raw}' не є числом")
    if integer and value != value.to_integral_value():
        raise ValueError(f"{name}='{raw}' має бути цілим числом")
    return int(value) if integer else value


def compound_table(principal, rate, years, compounding):
    """Повертає список рядків (рік, сума на початок, нараховано, сума на кінець)."""
    period_rate = rate / Decimal(100) / Decimal(compounding)
    rows = []
    balance = principal
    for year in range(1, years + 1):
        start = balance
        for _ in range(compounding):
            balance = balance * (1 + period_rate)
        rows.append((year, start, balance - start, balance))
    return rows


def money(value):
    q = value.quantize(CENT, rounding=ROUND_HALF_UP)
    return f"{q:,.2f}".replace(",", " ")


def main():
    try:
        principal = read_number("SUM", "10000")
        rate = read_number("RATE", "10")
        years = read_number("PERIODS", "5", integer=True)
        compounding = read_number("COMPOUNDING", "1", integer=True)
        if principal <= 0:
            raise ValueError("SUM має бути більше 0")
        if rate < 0:
            raise ValueError("RATE не може бути від'ємною")
        if years < 1:
            raise ValueError("PERIODS має бути не менше 1")
        if compounding < 1:
            raise ValueError("COMPOUNDING має бути не менше 1")
    except ValueError as err:
        print(f"Помилка вхідних даних: {err}", file=sys.stderr)
        return 1

    rows = compound_table(principal, rate, years, compounding)
    final = rows[-1][3]
    profit = final - principal

    line = "+------+-----------------+----------------+-----------------+"
    print("=" * len(line))
    print("  КАЛЬКУЛЯТОР СКЛАДНИХ ВІДСОТКІВ")
    print("=" * len(line))
    print(f"  Початкова сума:        {money(principal)} грн")
    print(f"  Річна ставка:          {rate}%")
    print(f"  Термін:                {years} р.")
    print(f"  Нарахування на рік:    {compounding}")
    print(f"  Формула:               S = P * (1 + r/n)^(n*t)")
    print(line)
    print("| Рік  | На початок, грн | Відсотки, грн  | На кінець, грн  |")
    print(line)
    for year, start, interest, end in rows:
        print(f"| {year:>4} | {money(start):>15} | {money(interest):>14} | {money(end):>15} |")
    print(line)
    print(f"  Кінцева сума:          {money(final)} грн")
    print(f"  Дохід (відсотки):      {money(profit)} грн")
    print(f"  Приріст:               {(profit / principal * 100).quantize(CENT)}%")
    print("=" * len(line))
    return 0


if __name__ == "__main__":
    sys.exit(main())
