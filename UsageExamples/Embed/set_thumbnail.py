from discord.ext import embed as eembed

embed = eembed.Embed()

"""
print(embed.thumbnail)

> None
"""

embed.set_thumbnail('https://embed-thumbnail.url/')

"""
print(embed.thumbnail)

> https://embed-thumbnail.url/
"""
