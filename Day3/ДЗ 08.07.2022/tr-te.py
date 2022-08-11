from translate import Translator
from langdetect import detect

a = input("Введите текст:")
b = detect(a)
translator = Translator(from_lang=str(b), to_lang="ru")
translation = translator.translate(a)

print(translation)
