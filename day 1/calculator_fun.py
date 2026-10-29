"""Day 1 · Step 1 — the same calculator, but the LOGIC is now a function, separate from input() and print().
Why it matters: a function can be called by other code — tests today, a web API in step 3.
Run:  python 02_calculator_function.py"""


def calculate(a: float, b: float, op: str) -> float:
    """Add, subtract, multiply or divide two numbers. Raises ValueError for bad input instead of printing."""
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


if __name__ == "__main__":
    # No keyboard needed: the function can be checked automatically.
    print("12 add 3 =", calculate(12, 3, "add"))
    print("12 div 3 =", calculate(12, 3, "div"))
    assert calculate(2, 5, "mul") == 10
    try:
        calculate(1, 0, "div")
    except ValueError as e:
        print("1 div 0  -> error:", e)
    print("all checks passed")