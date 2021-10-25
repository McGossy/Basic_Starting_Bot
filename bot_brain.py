import discord
from discord.ext import commands

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(
    command_prefix='!' # change this to change how to call bot commands
)

bot.load_extension("textCommands")
bot.load_extension("onMessage")


try:
    print('sys_flags')
    sys_flags = discord.SystemChannelFlags
    print(sys_flags)
except:
    print("That shit didn't work")




bot.run(token)