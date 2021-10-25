import discord
from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.is_ready = False

    @commands.Cog.listener()
    async def on_ready(self): # when bot is ready
        print('On Message ready')
        self.is_ready = True

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message): # on every message

        # Ignores all bots
        if message.author.bot:
            return

        # Bunch of stuff that can be used later
        guild = message.guild
        channel = message.channel
        channel_id = str(message.channel.id)
        author = message.author
        msg = message.content.lower()
        ignore = False


# finishes the setup of the cog so that the bot_brain can load it
def setup(bot: commands.Bot):
    bot.add_cog(OnMessage(bot))


