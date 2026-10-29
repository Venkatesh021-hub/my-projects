"""ee.py — the logic, in ONE place. The API (app.py) only calls these functions."""


def calculate(a: float, b: float, op: str) -> float:
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a * b
    if op == "div":
        if b == 0:
            raise ValueError("cannot divide by zero")
        return a / b
    raise ValueError(f"unknown operation '{op}' — use add, sub, mul or div")


def energy_cost(watts: float, hours: float, rate: float = 8.0) -> dict:
    """Units (kWh) and cost (₹) of running an appliance of `watts` for `hours`, at `rate` rupees per unit."""
    if watts <= 0 or not 0 < hours <= 24 or rate <= 0:
        raise ValueError("watts and rate must be positive, hours between 0 and 24")
    units = watts * hours / 1000                 # W × h = Wh; ÷ 1000 = kWh = units
    return {"units": round(units, 2), "cost_rs": round(units * rate, 2)}