import json
from json.decoder import JSONDecodeError
from functools import lru_cache


def str_is_illegal(s: str):
    # returns True if string contains any illegal characters
    legal_chars = ("_", "")
    return not all(map(lambda c: c in legal_chars or c.isalnum(), s))


def format_string(s: str):
    # replaces spaces and hyphens from string
    return s.casefold().replace("-", "").replace(" ", "")


def key_check(key: str):
    if len(key) <= 0:
        raise ValueError("key should atleast have a length of 1")

    if str_is_illegal(key):
        # 'key' should contain only alphabets and numbers
        raise ValueError(
            "Key should contain only alphanumeric character")

    return True

@lru_cache
async def search_key(key: str, channel):
    found_key, in_message = None, None
    async for message in channel.history(limit=None):
        cnt = message.content
        try:
            data = json.loads(str(cnt))
        except JSONDecodeError:
            print(f"-----\nJSONDecodeerror: {cnt}\n-----")
            continue
        if key in list(data.keys()):
            found_key = True
            in_message = message
            return found_key, in_message, data  # return useful data if keyis found
    return False, None, None  # return this if key is not found
