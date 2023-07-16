from discord.ext import commands, tasks
import reaction_handler
import discord

class CommandHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command() 
    async def help(self, ctx): 
        await ctx.send("**Help message**")


    @commands.command()
    async def add(self, ctx, left: int, right: int):
        await ctx.send(left + right)

    @commands.command()
    async def repeat(self, ctx, message: str):
        await ctx.send(message)

    @commands.command()
    async def play(self, ctx):
        if ctx.author.id == ctx.message.author.id:
            message = await ctx.send("play message")
            await message.add_reaction("👍")
            await message.add_reaction("👎")
            reaction_handler.set_command_message(ctx.author.id, message)


async def setup(client):
    await client.add_cog(CommandHandler(client))
    await reaction_handler.setup(client)
    print("Commands")