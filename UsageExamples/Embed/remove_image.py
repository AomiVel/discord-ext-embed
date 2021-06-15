from discord.ext import embed as eembed

embed = eembed.Embed(
    image='https://embed-image.url/'
)

"""
print(embed.image)

> https://embed-image.url/
"""

embed.remove_image()

"""
print(embed.image)

> None
"""
