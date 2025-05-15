
import uuid

PUBLIC_KEY = "YOUR_UNITPAY_PUBLIC_KEY"

def create_payment_link(user_id: int, amount: int = 90):
    label = f"{user_id}_{uuid.uuid4().hex[:6]}"
    link = f"https://unitpay.money/pay/{PUBLIC_KEY}?sum={amount}&account={user_id}&desc=Пополнение&label={label}"
    return link, label
