from googletrans import Translator


tran = Translator()

async def translate_user_text(text, to_lang):
    text = tran.translate(text, dest=to_lang)
    return text.text
