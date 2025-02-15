import time
import discord
from helper import generate_response

async def on_bot_ready(bot: discord.Bot):
    print(f"{bot.user} is ready and online!")
    await bot.sync_commands()  # Ensures all commands are up-to-date

def register_commands(bot: discord.Bot):
    print("Registering commands")
    @bot.slash_command(name="hello", description="Say hello to the bot")
    async def hello(ctx: discord.ApplicationContext):
        await ctx.respond("Heyyo!")

    @bot.slash_command(name="ping", description="Sends the bot's latency.")  # Creates a slash command
    async def ping(ctx):  # A slash command will be created with the name "ping"
        await ctx.respond(f"Pong! Latency is {bot.latency}")

    @bot.slash_command(name="chat", description="Send a message to the bot.")
    async def chat(ctx: discord.ApplicationContext, message: str):
        startTime = time.time()

        await ctx.defer(ephemeral=False)  # Ensure it's a public response and not ephemeral
        
        print(f"Received a chat message from user {ctx.author} (ID: {ctx.author.id}), message: {message}")
        response = generate_response(message)

        await ctx.followup.send(content=f"<@{ctx.author.id}> asked: {message} \n Response: {response}") 

        endTime = time.time()
        print(f"Time elapsed before response = {endTime - startTime:.2f} seconds")