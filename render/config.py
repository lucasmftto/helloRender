"""Settings module"""
import os

from dynaconf import Dynaconf, Validator

HERE = os.path.dirname(os.path.abspath(__file__))
mongodb_uri = os.getenv("MONGODB_URI")

settings = Dynaconf(
    envvar_prefix="render",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    # environments=["development", "production", "testing"],
    env_switcher="render_env",
    load_dotenv=False,
)


settings.configure(
    mongodb_uri=mongodb_uri,)

settings.validators.register(  # pyright: ignore
    Validator("SECRET_KEY", must_exist=True, is_type_of=str),
)

settings.validators.validate()  # pyright: ignore
