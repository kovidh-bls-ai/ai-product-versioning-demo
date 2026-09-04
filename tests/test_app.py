from src.app import translate


def test_translate():
    assert translate("Hello", "Spanish") == "[Spanish] Hello"
    assert translate("Goodbye", "French") == "[French] Goodbye"