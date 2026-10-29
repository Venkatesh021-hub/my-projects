"""Step 5 — the four HTTP methods on the appliance list, one call at a time.
Run:  python test_appliances.py"""
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def show(method, url, body=None):
    r = client.request(method, url, json=body)
    print(f"{method:<6} {url:<15} {str(body or ''):<48} -> {r.status_code} {r.json()}")


show("POST", "/appliances", {"name": "Room AC", "watts": 1500, "hours": 8})
show("POST", "/appliances", {"name": "Ceiling fan", "watts": 75, "hours": 10})
show("GET", "/appliances")
show("PUT", "/appliances/1", {"name": "Room AC", "watts": 1500, "hours": 6})
show("GET", "/appliances/1")
show("DELETE", "/appliances/2")
show("GET", "/appliances")
show("GET", "/appliances/2")
show("POST", "/appliances", {"name": "Geyser", "watts": 2000, "hours": 30})