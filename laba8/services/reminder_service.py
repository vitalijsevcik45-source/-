from sqlalchemy import select
from datetime import datetime
from db.database import async_session
from db.models import Reminder

async def create_reminder(user_id: int, chat_id: int, text: str, date: datetime):
    async with async_session() as session:
        reminder = Reminder(
            user_id=user_id,
            chat_id=chat_id,
            text=text,
            remind_at=date
        )
        session.add(reminder)
        await session.commit()

async def get_unsent_reminders():
    """Знаходить нагадування, час яких настав"""
    now = datetime.now()
    async with async_session() as session:
        # Шукаємо ті, де час менший за поточний і is_sent = False
        query = select(Reminder).where(
            Reminder.remind_at <= now,
            Reminder.is_sent == False
        )
        result = await session.execute(query)
        return result.scalars().all()

async def close_reminder(reminder_id: int):
    """Ставить мітку, що відправлено"""
    async with async_session() as session:
        reminder = await session.get(Reminder, reminder_id)
        if reminder:
            reminder.is_sent = True
            await session.commit()
