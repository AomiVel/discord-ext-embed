import discord
from discord.ext import embed as eembed

discord_embed = discord.Embed(...)

discordext_embed = eembed.Embed.from_discordEmbed(discord_embed)
