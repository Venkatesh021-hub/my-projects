"""Day 1 · Steps 3–5 — the calculator becomes a web API; Step 5 plugs in the appliance list from appliance.py.
Run:   uvicorn app:app --reload
Open:  http://127.0.0.1:8000/docs          ← interactive docs, generated for free
Try:   http://127.0.0.1:8000/calculate?a=12&b=3&op=div"""
from typing import Literal

from fastapi import FastAPI, HTTPException

import appliance
import ee

app = FastAPI(title="Campus Energy API", version="day-1")


@app.get("/")
def home():
    return {"message": "Campus Energy API is running. Open /docs to try it."}


# ── Steps 3–4: the calculator as an API ────────────────────────────────────────────────────────────
# GET = "give me something". The inputs travel in the address; the answer comes back as JSON.
# op may only be one of four words — anything else is refused with 422 before our function runs.
@app.get("/calculate")
def calculate(a: float, b: float, op: Literal["add", "sub", "mul", "div"]):
    try:
        return {"a": a, "b": b, "op": op, "result": ee.calculate(a, b, op)}
    except ValueError as e:                                   # our function refused it (e.g. divide by zero) → 400
        raise HTTPException(status_code=400, detail=str(e))


# ── Step 5: GET, POST, PUT, DELETE — the appliance list lives in its own file, appliance.py ──────────
app.include_router(appliance.router)
