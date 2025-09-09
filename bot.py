import os
import discord

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="YAKUZA Clan"))

bot.run(os.getenv("TOKEN"))
