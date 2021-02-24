import discord
import os

client = discord.Client();

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'yeets in {len(client.servers)} servers'))

@client.event
async def on_message(message):
  if message.author.bot:
    return
  if "yeet" in message.content.lower():
    await message.channel.send("yote")

client.run(os.getenv('BOT_TOKEN'))