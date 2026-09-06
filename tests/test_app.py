from src.app import translate


def test_translate():
    assert translate("Hello", "Spanish") == "[Spanish] Hello"


def test_unsupported_language():
    try:
        translate("Hello", "Japanese")
        assert False
    except ValueError:
        assert True