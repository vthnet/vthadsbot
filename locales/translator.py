from locales.en import TEXT as EN
from locales.ru import TEXT as RU
from locales.zh import TEXT as ZH
from locales.ar import TEXT as AR

LANGUAGES = {
    "en": EN,
    "ru": RU,
    "zh": ZH,
    "ar": AR,
}


def tr(language: str, key: str) -> str:

    if language not in LANGUAGES:
        language = "en"

    return LANGUAGES[language].get(
        key,
        EN.get(key, key)
    )