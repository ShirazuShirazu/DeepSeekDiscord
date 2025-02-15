import discord
import os  # default module
from dotenv import load_dotenv

load_dotenv()  # Load all the variables from the .env file
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.sync_commands()  # Ensures all commands are up-to-date

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Heyyo!")

@bot.slash_command(name="ping", description="Sends the bot's latency.")  # Creates a slash command
async def ping(ctx):  # A slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

# New chat command
@bot.slash_command(name="chat", description="Send a message to the bot.")
async def chat(ctx: discord.ApplicationContext, message: str):
    await ctx.respond(f"You said: {message}")  # Echo the message back

bot.run(os.getenv('TOKEN'))  # Run the bot with the token
