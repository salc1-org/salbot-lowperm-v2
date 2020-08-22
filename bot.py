import discord
import os
import helpers.pregenerator

from discord.ext import commands
from discord_logger import DiscordLogger


class Bot(commands.Bot):
    """A subclassed commands.Bot"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_extensions(self, cogs: list):
        """Loads a list of cogs"""
        for cog in cogs:
            try:
                super().load_extension(cog)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    bot = Bot(
        command_prefix="!",
        max_messages=10000,
        #allowed_mentions=discord.AllowedMentions(everyone=False, users=True, roles=False),
        help_command=commands.MinimalHelpCommand(dm_help=True, no_category="General")
    )

    cogs = [

    ]

    bot.load_extensions(cogs)
    bot.run(os.environ["TOKEN"])