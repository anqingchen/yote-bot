import discord

client = discord.Client();

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="yeets"))

@client.event
async def on_message(message):
  if "yeet" in message.content.lower():
    await message.channel.send("yote")

client.run("NzQzMTkyMDA1NzUxOTk2NTA2.XzRFfg.JNrZsNCKQy3fqqTRCIM6tTlQvbQ")