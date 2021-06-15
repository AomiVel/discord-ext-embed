from discord.ext import embed as eembed

embed = eembed.Embed()

"""
print(embed.author)

> None
"""

embed.set_author(
    name='author name',
    url='https://author.url/',
    icon_url='https://author-icon.url/'
)

"""
print(embed.author)

> {'name': 'author name', 'url': 'https://author.url/', 'icon_url': 'https://author-icon.url/'}
"""
