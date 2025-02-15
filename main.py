import discord 
import os
from dotenv import load_dotenv
load_dotenv()  # Load all the variables from the .env file
from botCommands import on_bot_ready, register_commands


print("Starting bot here")
bot = discord.Bot()
register_commands(bot)

@bot.event
async def on_ready():
    await on_bot_ready(bot)

if __name__ == "__main__":
    print("Starting discord bot")
    bot.run(os.getenv('TOKEN'))