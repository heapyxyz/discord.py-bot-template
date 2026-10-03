import discord
from discord import app_commands
from discord.ext import commands

from ..bot import Bot


class Hello(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Greets the user back.")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}!")


async def setup(bot: Bot):
    await bot.add_cog(Hello(bot))
