from typing import Any, Dict, Tuple, Union, Type
import os

from .exceptions import EnvGuardError, MissingEnvVarError, InvalidEnvVarTypeError


class EnvGuard:
    def __init__(self, schema: Dict[str, Union[Type, Tuple[Type, Any]]]):
        """
        schema: dict of var_name -> type or (type, default)
        """
        self.schema = schema
        self.config = {}

    def _convert_type(self, value: str, expected_type: Type) -> Any:
        try:
            if expected_type == bool:
                return value.lower() in ("1", "true", "yes", "on")
            return expected_type(value)
        except ValueError:
            raise InvalidEnvVarTypeError(value, expected_type)

    def load(self):
        for key, rule in self.schema.items():
            if isinstance(rule, tuple):
                expected_type, default = rule
                raw_value = os.getenv(key, None)

                if raw_value is None:
                    self.config[key] = default
                else:
                    self.config[key] = self._convert_type(raw_value, expected_type)

            else:
                expected_type = rule
                raw_value = os.getenv(key)

                if raw_value is None:
                    raise MissingEnvVarError(key)
                self.config[key] = self._convert_type(raw_value, expected_type)

        return EnvNamespace(self.config)


class EnvNamespace:
    def __init__(self, data: Dict[str, Any]):
        for k, v in data.items():
            setattr(self, k, v)

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return f"<EnvConfig {self.__dict__}>"
