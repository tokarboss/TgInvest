
# MMM Telegram Bot

## Установка
1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Установите токены в `main.py` и `payment.py`

3. Запустите бота:
```bash
python main.py
```

4. Запустите админку:
```bash
uvicorn admin_panel:app --reload
```

## Команды
- /start — регистрация
- /balance — показать баланс
- /invest — получить ссылку на оплату
