import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = "8206816109:AAEwi29LQgX9l21-pQh9zI-2KocXs0Dk0fA"
    # Назва файлу бази даних
    DB_URL = "sqlite+aiosqlite:///reminders.db"
