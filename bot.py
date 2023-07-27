import logging
from aiogram import Bot, Dispatcher, executor, types
from utils import translate_user_text
from bot_keyboards import choose_lang_btn


API_TOKEN = '6233774027:AAFpgeX3IZ-r0GNXmiNDGm2vcge3mjOCIBA'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Salom")


@dp.message_handler(content_types=['text'])
async def get_user_text(message: types.Message):
    print(get_user_text)
    text = message.text
    result = await translate_user_text(text, "uz")
    btn = await choose_lang_btn()
    await message.answer(result, reply_markup=btn)


@dp.callback_query_handler(text="lang_ru")
async def to_ru(call: types.CallbackQuery):
    text = call.message.text
    result = await translate_user_text(text, "ru")
    btn = await choose_lang_btn()
    await call.message.answer(result, reply_markup=btn)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
