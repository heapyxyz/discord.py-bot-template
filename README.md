# discord.py-template

A simple Discord.py bot template I use for all of my bots. Feel free to use and modify it. `uv` is required to run this bot.

## Usage

1. **Get a Bot Token:**  
   Create a bot in [Discord Developer Portal](https://discord.com/developers/applications/) and copy its token.

2. **Create Environment File:**  
   Copy `.env.example` file as `.env`.

3. **Add the Token:**  
   Paste the token into the `.env` file. It should look like this:

   ```bash
   # https://discord.com/developers/applications
   BOT_TOKEN="MTM0NTY3ODkwMTIzNDU2Nzg5.CDEfGH.IJKLMN_opq1234567890abcdef"
   ```

4. **Install Dependencies:**

   ```bash
   uv sync
   ```

5. **Run the Bot:**

   ```bash
   uv run bot
   ```

## Managing Cogs

The bot automatically detects (recursively) and loads cogs inside `src/bot/cogs/` directory. An example `/hello` command is available in [`hello.py`](./src/bot/cogs/hello.py) to get you started.

For more information, read [discord.py documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html).
