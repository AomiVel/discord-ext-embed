from discord.ext import embed as eembed

embed = eembed.Embed()

"""
print(embed.image)

> None
"""

embed.set_image('https://embed-image.url/')

"""
print(embed.image)

> https://embed-image.url/
"""
