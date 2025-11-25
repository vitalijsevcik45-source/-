from aiogram import Bot
from services.reminder_service import get_unsent_reminders, close_reminder


async def check_reminders(bot: Bot):
    reminders = await get_unsent_reminders()

    for r in reminders:
        try:
            await bot.send_message(r.chat_id, f"⏰ <b>Нагадування:</b>\n{r.text}")
            await close_reminder(r.id)
        except Exception as e:
            print(f"Помилка відправки {r.id}: {e}")
