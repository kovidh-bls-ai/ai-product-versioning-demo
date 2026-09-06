from src.app import translate


def test_translate():
    assert translate("Hello", "English", "Spanish") == "[English -> Spanish] Hello"


def test_unsupported_language():
    try:
        translate("Hello", "English", "Japanese")
        assert False
    except ValueError:
        assert True


def test_translate_case_insensitive():
    assert translate("Hello", "English", "Spanish") == "[English -> Spanish] Hello"