from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from services.reminder_service import create_reminder

router = Router()


class Form(StatesGroup):
    waiting_for_text = State()
    waiting_for_date = State()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привіт! Напиши /new щоб створити нагадування.")


@router.message(Command("new"))
async def cmd_new(message: Message, state: FSMContext):
    await message.answer("Що тобі нагадати? (Напиши текст)")
    await state.set_state(Form.waiting_for_text)


@router.message(Form.waiting_for_text)
async def process_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer(
        "На коли встановити? \n"
        "Введи формат: <b>РРРР-ММ-ДД ГГ:ХХ</b>\n"
        "Приклад: 2025-11-26 14:30",
        parse_mode="HTML"
    )
    await state.set_state(Form.waiting_for_date)


@router.message(Form.waiting_for_date)
async def process_date(message: Message, state: FSMContext):
    date_str = message.text
    try:
        # Парсимо дату
        remind_at = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        data = await state.get_data()
        text = data['text']

        # Зберігаємо
        await create_reminder(message.from_user.id, message.chat.id, text, remind_at)

        await message.answer(f"✅ Готово! Нагадаю про це {remind_at}")
        await state.clear()

    except ValueError:
        await message.answer("❌ Невірний формат. Спробуй ще раз: 2025-11-26 14:30")
