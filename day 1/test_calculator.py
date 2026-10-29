"""Steps 3–4 — call the calculator API from Python, the way a browser or another program would.
Run:  python test_calculate.py"""
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)
for url in ["/calculate?a=12&b=3&op=div", "/calculate?a=12&b=3&op=mul", "/calculate?a=1&b=0&op=div", "/calculate?a=2&b=3&op=pow"]:
    r = client.get(url)
    print(f"GET {url:<28} -> {r.status_code} {r.json()}")