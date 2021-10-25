from DiscordDatabase.common_functions import format_string
from DiscordDatabase.database import Database


class DiscordDatabase:
    # This class takes care of creating categories and channels for the database
    def __init__(self, client, guild_id) -> None:
        self.guild_id = guild_id
        self.client = client

    async def __create(self, category_name: str, channel_name: str):
        category_name = format_string(category_name)  # No spaces allowed
        channel_name = format_string(channel_name)   # No spaces allowed

        if len(category_name) <= 0:
            raise ValueError("category_name should atleast have a length of 1")
        if len(channel_name) <= 0:
            raise ValueError("channel_name should atleast have a length of 1")

        ##### CATEGORY #####
        category = list(filter(lambda c: c.name.casefold()
                        == category_name, self.__GUILD.categories))
        # Returns a list of categories which have same name as 'category_name'
        # Should return a list containg only one category with a unique name
        # Empty list means category does not exists

        if category == []:
            # Create category if doesnot exist
            category = await self.__GUILD.create_category(category_name)
        else:
            # Get category object if exists
            category = category[0]

        ##### CHANNEL #####
        channel = list(filter(lambda c: c.name ==
                       channel_name, category.channels))
        # Returns a list of channels under the category which have same name as 'channel_name'
        # Should return a list containg only one channel with a unique name
        # Empty list means channel doesnot exists

        if channel == []:
            # Create a new channel under category
            channel = await category.create_text_channel(channel_name)
        else:
            # Get existing channel
            channel = channel[0]

        return category, channel

    async def new(self, category_name, channel_name):
        await self.client.wait_until_ready()
        self.__GUILD = self.client.get_guild(self.guild_id)
        category, channel = await self.__create(category_name, channel_name)
        # This is the actual class that takes care of setting and getting data from the database
        return Database(category, channel)
