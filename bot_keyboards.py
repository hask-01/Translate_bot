from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def choose_lang_btn():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("UZ", callback_data="lang_uz"),
        InlineKeyboardButton("RU", callback_data="lang_ru"),
        InlineKeyboardButton("EN", callback_data="lang_en"),
    )
    return btn


