import os
import sys
import discord
import asyncio
from discord.ext import commands
from pathlib import Path

intents = discord.Intents.default()
# intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
commands_dir = Path(__file__).resolve().parent.parent / 'commands'

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def load_extensions():
    for filename in os.listdir(commands_dir):
        if filename.endswith('.py') and not filename.startswith('_'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}: {e}')

async def main():
    try:
        async with bot:
            await load_extensions()
            await bot.start(os.getenv("DISCORD_TOKEN", ""))
    except KeyboardInterrupt:
        print("\n🛑 Beende Bot sauber...")

        # Optional: zusätzliche Aufräumarbeiten hier
        await bot.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("❌ Bot wurde manuell gestoppt.")