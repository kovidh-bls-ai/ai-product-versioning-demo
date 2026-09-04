def translate(text: str, target_language: str) -> str:
    return f"[{target_language}] {text}"


if __name__ == "__main__":
    print(translate("Hello", "Spanish"))