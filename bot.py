import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import logging
import logging.handlers
import command_handler
import reaction_handler
#import tracemalloc


#tracemalloc.start()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREIFX= os.getenv('PREFIX')
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix=PREIFX, intents=intents, help_command=None)


@client.event
async def on_ready():
    await command_handler.setup(client)
    await reaction_handler.setup(client)
    activity = discord.Activity(name="To Moe", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print(f'We have logged in as {client.user}')
    
    

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.startswith('$play'):
        embedGame = discord.Embed(title="Tic Tac Toe", description="This bot was made by Uncle Moe", color=0x00ff00)
        embedGame.add_field(name="Players", value="Player one: @test against Player two: @test2", inline=False)
        embedGame.add_field(name="The Game", value=":green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:\n:green_square: :one: :green_square:I:green_square: :two: :green_square:I:green_square: :three: :green_square:\n:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:", inline=False)
        embedGame.add_field(name="", value=":green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:\n:green_square: :four: :green_square:I:green_square: :five: :green_square:I:green_square: :six: :green_square:\n:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:", inline=False)
        embedGame.add_field(name="", value=":green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:\n:green_square: :seven: :green_square:I:green_square: :eight: :green_square:I:green_square: :nine: :green_square:\n:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:I:green_square: :green_square: :green_square:", inline=False)        
        msg = await message.channel.send(embed=embedGame)
        emoji_numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        number_of_responses = 9
        for counter in range(number_of_responses):
            await msg.add_reaction(emoji_numbers[counter])
        
    await client.process_commands(message)





logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)



client.run(TOKEN, log_handler=None)
