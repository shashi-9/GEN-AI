from langdetect import detect, LangDetectException

print("===== Language Detection Program =====")

text = input("Enter a sentence: ")

try:
    language = detect(text)

    language_names = {
        "en": "English",
        "te": "Telugu",
        "hi": "Hindi",
        "ta": "Tamil",
        "kn": "Kannada",
        "ml": "Malayalam",
        "fr": "French",
        "de": "German",
        "es": "Spanish",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "ja": "Japanese",
        "ko": "Korean",
        "zh-cn": "Chinese",
        "ar": "Arabic"
    }

    print("Detected Language Code:", language)
    print("Detected Language:", language_names.get(language, "Unknown Language"))

except LangDetectException:
    print("Unable to detect the language.")