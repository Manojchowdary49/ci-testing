
def add(a, b):
    return a + b

def place_order(price, quantity):
    if price <= 0 or quantity <= 0:
        raise ValueError("Price and quantity must be positive")
    return price * quantity

def process_order(price, quantity, payment_success):
    total = place_order(price, quantity)
    if not payment_success:
        return {"status": "failed", "total": total}
    return {"status": "success", "total": total}
