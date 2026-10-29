"""Day 1 · Step 2 — a calculator everyone needs: what does an appliance cost to run?
Units: power in watts (W) · 1,000 W = 1 kW · energy in kWh · 1 kWh = 1 "unit" on the electricity bill.
Run:  python 03_energy_cost.py"""


def energy_cost(watts: float, hours: float, rate: float = 8.0) -> dict:
    """Units (kWh) and cost (₹) of running an appliance of `watts` for `hours`, at `rate` rupees per unit."""
    if watts <= 0 or not 0 < hours <= 24 or rate <= 0:
        raise ValueError("watts and rate must be positive, hours between 0 and 24")
    units = watts * hours / 1000                 # W × h = Wh; ÷ 1000 = kWh = units
    return {"units": round(units, 2), "cost_rs": round(units * rate, 2)}


if __name__ == "__main__":
    print("1.5 kW AC, 8 hours      ->", energy_cost(1500, 8))
    print("75 W ceiling fan, 10 h  ->", energy_cost(75, 10))
    print("2 kW geyser, 30 minutes ->", energy_cost(2000, 0.5))