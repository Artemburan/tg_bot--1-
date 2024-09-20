from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from app.keyboards.global_menu import global_menu_keyboard_builder

start_router = Router()

@start_router.message(CommandStart())
async def start_heandler(message: Message, state: FSMContext):
    keybord = global_menu_keyboard_builder()
    return message.answer(
        text=f"Вітаю у ветеренарії '{message.from_user.full_name}'",
        reply_markup=keybord
        )