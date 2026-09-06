SUPPORTED_LANGUAGES = ["Spanish", "French", "German"]


def translate(text: str, target_language: str) -> str:
    if target_language.capitalize() not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {target_language}")

    target_language = target_language.capitalize()

    return f"[{target_language}] {text}"

if __name__ == "__main__":
    print(translate("Hello", "Spanish"))