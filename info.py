from os import environ, getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "1296545302"))
API_ID = int(getenv("API_ID", "24607450"))
API_HASH = str(getenv("API_HASH", "204768fe292a431ee267aebaa1dbbd11"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7369577010:AAEII9dAkQITsMAb6YxU5EOavdJ7kKYtlm8"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://replacewithyourmongodb:replacewithyourmongodb@cluster0.zi78j51.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
