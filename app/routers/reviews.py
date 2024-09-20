from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.forms.review import ReviewForm
from app.data import list_files, files_actions


review_router = Router()

@review_router.message(F.text == "Показати всі відгуки")
async def show_reviews(message: Message, state: FSMContext):
    reviews = files_actions.open_file(list_files.REVIEWS)

    msg = ""
    for i, review in enumerate(reviews, start=1):
        msg += f"{i}. {review}\n"

    await message.answer(text=msg or "Відгуків ще немає")


@review_router.message(F.text == "Додати новий відгук")
async def add_review(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(ReviewForm.text)
    await message.answer(text="Введіть свій відгук")

@review_router.message(ReviewForm.text)
async def save_new_review(message: Message, state: FSMContext):
    data = await state.update_data(text=message.text)
    await state.clear()
    reviews = files_actions.open_file(list_files.REVIEWS)
    reviews.append(data.get("text"))
    files_actions.save_file(reviews, list_files.REVIEWS)
    await message.answer(text="Ваш відгук успішно додано")