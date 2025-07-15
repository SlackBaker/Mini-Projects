import json

class Localization:
    def __init__(self, language_code="ua"):
        try:
            with open(f"lang_{language_code}.json", encoding="utf-8") as f:
                self.translations = json.load(f)
        except FileNotFoundError:
            print("⚠️ Language file not found, using fallback.")
            self.translations = {}

    def t(self, key):
        return self.translations.get(key, key)