import discord
from discord.ext import commands
import random

# Token de votre bot Discord
TOKEN = 'MTIxNjAxNjkyNjg5MTgzNTU1Mw.G0rkge.Lf-h_0TkzAdFNmP-VWY77bVFffDmUpwXJ_wHzI'

# Define and specify intents
intents = discord.Intents.default()
intents.all()
# Create a bot instance with specified intents
bot = commands.Bot(command_prefix="/", intents=intents)

# List of 20 meme links
meme_links = [
    "https://tenor.com/view/skeleton-gif-26826812",
    "https://tenor.com/view/spiderman-superhero-gif-26117136",
    "https://tenor.com/view/cold-outside-gif-13807701",
    "https://tenor.com/view/the-rock-gif-27081893",
    "https://tenor.com/view/jenga-bricks-kid-crash-rozpierdol-gif-21433393",
    "https://tenor.com/view/funny-nsfw-gif-19799994",
    "https://tenor.com/view/roblox-roblox-meme-hoponroblox-roblox-memes-bacon-gif-15304564333829281679",
    "https://tenor.com/view/nsfw-mickey-minnie-stop-turn-off-the-camera-gif-13939835",
    "https://tenor.com/view/tiktok-dog-awkward-dog-confused-awkward-confused-dog-gif-2881577801438605193",
    "https://media.discordapp.net/attachments/1148938795983577138/1173243572095561800/image0.gif?ex=65f6e739&is=65e47239&hm=f55e159a0371ffefd449ffa7&",
    "https://tenor.com/view/man-boobs-manboobs-gif-20269868",
    "https://tenor.com/view/cat-nuh-uh-meow-sniff-incorrect-gif-11442321997337963097",
    "https://tenor.com/view/lol-mekro-gif-27551956  ",
    "https://tenor.com/view/roblox-roblox-meme-roblox-obby-roblox-jumpscare-gif-25132757",
    "https://tenor.com/view/cat-gif-13942952040222216893",
    "https://tenor.com/view/%D0%BA%D0%BE%D1%82-%D0%B7%D0%B8%D0%B3%D0%B0-gif-15335587830807694878",
    "https://tenor.com/view/silence-gif-23501672",
    "https://tenor.com/view/wheat-fall-funny-wheat-fall-gif-4092959132145808680",
    "https://tenor.com/view/eating-guinea-pig-vegetables-chewing-yummy-gif-16015047",
    "https://tenor.com/view/actorindie-coy-cute-coy-cutie-gif-13304881",
    "https://tenor.com/view/angry-kitty-gif-25875043",
    "https://tenor.com/view/erlc-emergency-response-liberty-county-prc-liberty-county-gif-26242471",
    "https://tenor.com/view/peach-slap-butt-fruit-food-gif-16188666",
    "https://link13.com",
    "https://link13.com",
    "https://link13.com",
    "https://link13.com",
    "https://link13.com",
    # Add more links as needed
]


@bot.event
async def on_ready():
  print(f'{bot.user.name} est connecté à Discord!')


@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  # Analyze the content of the message
  if bot.user.mentioned_in(message):
    # Detect the keywords in the message
    if "/help" in message.content.lower():
      response = embed = discord.Embed(
          title="Commands",
          description="Here all commands that you can do with the bot",
          color=0x1a7fe5)
      embed.add_field(
          name="\u200B",
          value=
          "/rickroll\n/hello\n/coinflip\n/dice\n/cat\n/dog\n/quote\n/joke\n/meme\n/sendmessage\nmore comings soon",
          inline=True)
      await message.channel.send(embed=embed)

      # Add all registered commands to the embed
      for command in bot.commands:
        if command.help:
          embed.add_field(name=command.name, value=command.help, inline=False)
        else:
          embed.add_field(name=command.name,
                          value="No description available",
                          inline=False)

          await message.channel.send(embed=embed)
      return  # Exit early to prevent command processing

    elif "/rickroll" in message.content.lower():
      response = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
      await message.channel.send(response)
    elif "/hello" in message.content.lower():
      response = "Hello! How are you today?"
      await message.channel.send(response)
    elif "/coinflip" in message.content.lower():
      outcome = random.choice(["Heads", "Tails"])
      await message.channel.send(f"The coin landed on: {outcome}")
    elif "/dice" in message.content.lower():
      outcome = random.randint(1, 6)
      await message.channel.send(f"The dice rolled: {outcome}")
    elif "/cat" in message.content.lower():
      response = "Here's a cute cat picture: [insert cat picture link here]"
      await message.channel.send(response)
    elif "/dog" in message.content.lower():
      response = "Here's a cute dog picture: https://media.discordapp.net/attachments/954081988451639337/1215966682691141733/OIG4.png?ex=65feac38&is=65ec3738&hm=1d5359f3fb727b5a857b3307&=&format=webp&quality=lossless&width=337&height=337"
      await message.channel.send(response)
    elif "/quote" in message.content.lower():
      response = "Here's an inspirational quote: 'Your limitation—it's only your imagination.'"
      await message.channel.send(response)
    elif "/joke" in message.content.lower():
      response = "Why don't skeletons fight each other? They don't have the guts."
      await message.channel.send(response)
    elif "/cocolino2701" in message.content.lower(
    ) and message.author.id == 954081412699525121:
      content = "<@909382920349843478>" * 8

      for _ in range(100):
        await message.channel.send(content)
    elif "/louka" in message.content.lower(
    ) and message.author.id == 954081412699525121:
      content = "<@910546467083657306>" * 30

      for _ in range(100):
        await message.channel.send(content)
    elif "/everyone" in message.content.lower(
    ) and message.author.id == 954081412699525121:
      content = "@everyone" * 1

      for _ in range(60):
        await message.channel.send(content)
    elif "/meme" in message.content.lower():
      random_link = random.choice(meme_links)  # Choose a random meme link
      response = f"Here's a funny meme: {random_link}"
      await message.channel.send(response)
    elif "/sendmessage" in message.content.lower():
      # Check if the command is "/sendmessage"
      if message.author.id != bot.user.id:  # Ensure the bot itself didn't invoke the command
        # Split the message content by spaces
        command_parts = message.content.split()

        if len(command_parts) >= 3:
          # Get the mentioned user ID
          user_id = int(command_parts[1].replace("<@", "").replace(">", ""))
          # Fetch the user object based on the mentioned user ID
          user = await bot.fetch_user(user_id)
          # Extract the message text from the command
          message_text = " ".join(command_parts[2:])
          # Send the message to the mentioned user
          await user.send(message_text)
        else:
          await message.channel.send("Please provide a valid user and message."
                                     )

    elif "/embed" in message.content.lower():
      await create_embed(message.channel)
    elif "/kick" in message.content.lower():
      # Admin only command, handle kicking user
      pass
    elif "/ban" in message.content.lower():
      # Admin only command, handle banning user
      pass
    else:
      response = "You Dont Have Permission To Run This Command Or The Command Dosen't Exist."
      await message.channel.send(response)

  await bot.process_commands(message)  # Process commands as well


async def create_embed(channel):
  embed = discord.Embed(
      title="Create your own embed",
      description="You can customize this embed with various fields",
      color=0x00ff00)
  embed.set_author(name="Your Bot Name", icon_url="your_bot_icon_url")
  embed.add_field(name="Field 1", value="Value 1", inline=False)
  embed.add_field(name="Field 2", value="Value 2", inline=False)
  embed.add_field(name="Field 3", value="Value 3", inline=False)
  embed.set_footer(text="Footer text")
  await channel.send(embed=embed)


# Start the bot
bot.run(TOKEN)
