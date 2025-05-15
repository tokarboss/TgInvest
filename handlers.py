
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from db import *
from payment import create_payment_link
from usd_rate import get_usd_rate

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    user_id = message.from_user.id
    args = message.text.split()
    referrer_id = int(args[1]) if len(args) > 1 and args[1].isdigit() else None
    add_user(user_id, referrer_id)
    await message.answer("Добро пожаловать! Используйте /invest для пополнения баланса.")

@router.message(Command("balance"))
async def cmd_balance(message: Message):
    balance = get_balance(message.from_user.id)
    await message.answer(f"Ваш баланс: {balance} очков.")

@router.message(Command("invest"))
async def cmd_invest(message: Message):
    user_id = message.from_user.id
    link, label = create_payment_link(user_id)
    save_payment_label(user_id, label)
    await message.answer(f"Ссылка для оплаты: {link}")

@router.message(Command("market"))
async def cmd_market(message: Message):
    offers = get_market_offers()
    usd = get_usd_rate()
    price_per_point = round(usd * 0.0009, 4)
    text = f"Актуальный курс: {usd}₽ за $1
Цена 1 очка: {price_per_point}₽

Объявления:
"
    for offer in offers:
        text += f"ID {offer[0]}: {offer[2]} очков — {offer[3]}₽ (@{offer[1]})
"
    await message.answer(text if offers else "Нет активных предложений.")
