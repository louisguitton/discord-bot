import os
from discord.ext.commands import Bot
from dotenv import load_dotenv


client = Bot(command_prefix="!")


@client.command(name="clear", help="this command will clear msgs")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


if __name__ == "__main__":
    load_dotenv()
    client.run(os.environ.get("DISCORD_BOT_TOKEN"))
