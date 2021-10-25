import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class TextCommands(commands.Cog):
    """A few simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.is_ready = False

    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands ready')
        self.is_ready = True

    # basic command
    @commands.command(name="test")
    async def test(self, ctx: commands.Context):
        await ctx.message.channel.send("It works!")

    # basic command that checks the permissions of the user
    @has_permissions(administrator=True)
    @commands.command(name="admin")
    async def is_admin(self, ctx: commands.Context):
        await ctx.message.channel.send("You're an admin!")

    # how to handle errors if you think your command will easily encounter them
    @is_admin.error
    async def is_admin_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("You're not an admin!")


# finishes the setup of the cog so that the bot_brain can load it
def setup(bot: commands.Bot):
    bot.add_cog(TextCommands(bot))