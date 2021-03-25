TOKEN = ""
# import the module
from discord.ext import commands
from prsaw import RandomStuff

bot = commands.Bot(command_prefix=">")
rs = RandomStuff(async_mode = True)

@bot.event
async def on_ready():
    print("Bot is ready!")

#ERRORHANDLING
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments.")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'**{round(client.latency * 1000)}**ms.')
    await ctx.message.add_reaction('📶')

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return

    if message.channel.id == "PUTYOUROWNCHANNELIDHERE but remove string":
        response = await rs.get_ai_response(message.content)
        await message.reply(response)

    await bot.process_commands(message)

bot.run(TOKEN)