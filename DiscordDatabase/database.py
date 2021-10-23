import json
from DiscordDatabase.common_functions import key_check, search_key


class Database:
    def __init__(self, category_object, channel_object) -> None:
        self.__category = category_object
        self.__channel = channel_object  # Channel in which all key value pairs are stored

    def get_channel_id(self):
        return self.__channel.id

    def get_category_id(self):
        return self.__category.id

    async def set(self, key: str, value):
        key_check(key)
        if len(str(value)) <= 0:
            raise ValueError("value should atleast have a length of 1")

        value_type = value.__class__.__name__

        # True/False should become 1/0
        # integers and floats should become strings
        # In the end everything is stored as a string, along with an identifier
        """ Every message should look like this
        {key:value,type:'...'}
        """

        # conversion into storable string
        if value_type == 'bool':
            value = int(value)
        if value_type in ('int', 'float'):
            value = str(value)

        found_key, in_message, data = await search_key(key, self.__channel)
        if found_key:
            data[key] = value
            data["type"] = value_type
            await in_message.edit(content=json.dumps(data))
        else:
            data = {key: value, "type": value_type}
            await self.__channel.send(json.dumps(data))

    async def get(self, key: str):
        key_check(key)
        found_key, in_message, data = await search_key(key, self.__channel)
        if found_key:
            value = data[key]
            value_type = data["type"]

            if value_type == 'int':
                value = int(value)
            elif value_type == 'float':
                value = float(value)

            if value_type == 'bool':
                value = bool(int(value))
        else:
            value = None
        return value

    async def delete(self, key: str):
        key_check(key)
        found_key, in_message, data = await search_key(key, self.__channel)
        if found_key:
            await in_message.delete()
            return data[key]  # return the value of that key after deleting
        return None  # returns None if key waws not found and nothing was deleted
