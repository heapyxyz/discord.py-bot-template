import discord
from discord.ext import commands
from pathlib import Path


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="/", intents=intents)

    async def on_ready(self):
        if self.user:
            print(f"Logged in as @{self.user.name}")

    async def setup_hook(self):
        current = Path(__file__).parent
        package = current.name

        for path in current.glob("cogs/**/*.py"):
            if path.name.startswith("__"):
                continue

            relative = (
                path.relative_to(current).with_suffix("").as_posix().replace("/", ".")
            )
            cog = f"{package}.{relative}"

            await self.load_extension(cog)
            print(f"Loaded {path.name} ({cog})")

        await self.tree.sync()
