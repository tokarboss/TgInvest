
from fastapi import FastAPI, Request, Form
from db import add_balance

app = FastAPI()
ADMIN_ID = 6637727338

@app.post("/admin/add")
async def admin_add(user_id: int = Form(...), amount: int = Form(...), telegram_id: int = Form(...)):
    if telegram_id != ADMIN_ID:
        return {"error": "Unauthorized"}
    add_balance(user_id, amount)
    return {"message": f"Начислено {amount} очков пользователю {user_id}"}
