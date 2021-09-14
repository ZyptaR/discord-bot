import logging
logging.basicConfig(level="INFO")

import discord
from discord.ext import commands

from image_cog import image_cog
from music_cog import music_cog

Bot = commands.Bot(command_prefix='/')

Bot.add_cog(image_cog(Bot))
Bot.add_cog(music_cog(Bot))

token = "ODg3MzkyNjI3ODQwOTEzNDM4.YUDeyQ.NSNBQQkwnd-wsp-QOKQrccKUzBE"
with open("token.txt") as file:
    token = file.read()
Bot.run(token)