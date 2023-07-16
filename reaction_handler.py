from discord.ext import commands, tasks

command_message = {}

def set_command_message(user_id, message):
    command_message[user_id] = message

class ReactionHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.client.user:
            return
        
        message = reaction.message
        user_id = user.id

        # Perform actions based on the reaction and user
        if user_id in command_message and message.id == command_message[user_id].id:
            if str(reaction.emoji) == "👍":
                await reaction.message.channel.send(f"{user.mention} reacted with 👍")
                print("done")
                # Additional actions for 👍 reaction
            elif str(reaction.emoji) == "👎":
                await reaction.message.channel.send(f"{user.mention} reacted with 👎")
                # Additional actions for 👎 reaction

async def setup(client):
    await client.add_cog(ReactionHandler(client))
    print("Reactions")