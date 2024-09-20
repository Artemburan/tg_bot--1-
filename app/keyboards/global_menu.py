from aiogram.utils.keyboard import ReplyKeyboardBuilder


def global_menu_keyboard_builder():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Показати всіх тваринок")
    builder.button(text="Показати вилікуваних тваринок")
    builder.button(text="Показати всі відгуки")
    builder.button(text="Додати нову тваринку")
    builder.button(text="Додати відгук")
    builder.adjust(1)
    return builder.as_markup()