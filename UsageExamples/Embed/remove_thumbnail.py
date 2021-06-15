from discord.ext import embed as eembed

embed = eembed.Embed(
    image='https://embed-thumbnail.url/'
)

"""
print(embed.thumbnail)

> https://embed-thumbnail.url/
"""

embed.remove_thumbnail()

"""
print(embed.thumbnail)

> None
"""
