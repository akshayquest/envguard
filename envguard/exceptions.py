class EnvGuardError(Exception):
    """Base class for EnvGuard exceptions."""
    pass


class MissingEnvVarError(EnvGuardError):
    def __init__(self, var_name: str):
        super().__init__(f"Missing required environment variable: {var_name}")


class InvalidEnvVarTypeError(EnvGuardError):
    def __init__(self, value: str, expected_type: type):
        super().__init__(f"Invalid type for value '{value}'. Expected type: {expected_type.__name__}")
