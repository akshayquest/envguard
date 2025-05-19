import os
import pytest
from envguard import EnvGuard
from envguard.exceptions import MissingEnvVarError, InvalidEnvVarTypeError


def test_valid_env(monkeypatch):
    monkeypatch.setenv("PORT", "8000")
    monkeypatch.setenv("DEBUG", "true")

    config = EnvGuard({
        "PORT": int,
        "DEBUG": bool
    }).load()

    assert config.PORT == 8000
    assert config.DEBUG is True


def test_missing_required(monkeypatch):
    monkeypatch.delenv("REQUIRED_VAR", raising=False)

    with pytest.raises(MissingEnvVarError):
        EnvGuard({"REQUIRED_VAR": str}).load()


def test_invalid_type(monkeypatch):
    monkeypatch.setenv("SHOULD_BE_INT", "not_an_int")

    with pytest.raises(InvalidEnvVarTypeError):
        EnvGuard({"SHOULD_BE_INT": int}).load()


def test_default_value(monkeypatch):
    monkeypatch.delenv("OPTIONAL_VAR", raising=False)

    config = EnvGuard({"OPTIONAL_VAR": (str, "default")}).load()
    assert config.OPTIONAL_VAR == "default"
