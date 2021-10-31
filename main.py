import os
from discord.ext.commands import Bot
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

client = Bot(command_prefix="!")


@client.event
async def on_ready():
    logging.info("Connected")
    logging.info(f"Logged in as: {client.user} - {client.guilds}")


@client.command(name="clear", help="Clears last [amount] messages in the channel")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


if __name__ == "__main__":
    load_dotenv()
    client.run(os.environ.get("DISCORD_BOT_TOKEN"))
