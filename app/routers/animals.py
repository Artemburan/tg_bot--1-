from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.data import files_actions, list_files
from app.keyboards.animals import anims_keyboard_builder, anim_actions_keyboards
from app.forms.animal import AnimalForm


anims_router = Router()


@anims_router.message(F.text == "Показати всіх тваринок")
async def show_animals(message: Message, state: FSMContext):
    animals = files_actions.open_file()
    keyboard = anims_keyboard_builder(animals)
    await message.answer(
        text="Виберіть тваринку",
        reply_markup=keyboard
    )


@anims_router.callback_query(F.data.startswith("anim_"))
async def animal_actions(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    keyboard = anim_actions_keyboards(animal)
    await callback.message.answer(
        text=animal,
        reply_markup=keyboard
        )


@anims_router.callback_query(F.data.startswith("cured_anim_"))
async def cured_animal(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.cured_animal(animal)
    await callback.message.answer(text=msg)


@anims_router.callback_query(F.data.startswith("del_anim_"))
async def del_animal(callback: CallbackQuery, state: FSMContext):
    animal = callback.data.split("_")[-1]
    msg = files_actions.del_animal(animal)
    await callback.message.answer(text=msg)


@anims_router.message(F.text == "Додати нову тваринку")
async def add_animal(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(AnimalForm.name)
    await message.answer(text="Введіть назву тваринки")


@anims_router.message(AnimalForm.name)
async def save_new_animal(message: Message, state: FSMContext):
    data = await state.update_data(name=message.text)
    await state.clear()
    msg = files_actions.add_animal(data.get("name"))
    await message.answer(text=msg)


@anims_router.message(F.text == "Показати вилікуваних тваринок")
async def show_cured_anims(message: Message, state: FSMContext):
    cured_animals = files_actions.open_file(list_files.CURED_ANIMALS)

    msg = ""
    for i, prod in enumerate(cured_animals, start=1):
        msg += f"{i}. {prod}\n"

    await message.answer(text=msg)